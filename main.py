from etl.pipeline import ETLPipeline
from validation.split import TimeSeriesSplit
from validation.backtest_runner import BacktestRunner
from strategy.moving_average import MovingAverageCrossStrategy

from risk.performance import PerformanceReport

# ML imports
from ml.feature_pipeline import FeaturePipeline, create_labels
from ml.model import MLModel
from ml.signal_filter import MLSignalFilter


# ------------------------
# 1. LOAD DATA
# ------------------------
pipeline = ETLPipeline(data_dir="data/")
data = pipeline.run("data/raw/market_data.csv")


# ------------------------
# 2. TRAIN / TEST SPLIT
# ------------------------
splitter = TimeSeriesSplit(train_ratio=0.7)
train_data, test_data = splitter.split(data)


# ------------------------
# 3. TRAIN ML MODEL (OPTIONAL)
# ------------------------
feature_pipeline = FeaturePipeline()

from ml.feature_pipeline import FeaturePipeline, create_labels
from ml.model import MLModel

feature_pipeline = FeaturePipeline()

all_X = []
all_y = []

for symbol, df_symbol in train_data.groupby("symbol"):

    df_symbol = df_symbol.sort_index()

    features = feature_pipeline.transform(df_symbol)
    labels = create_labels(df_symbol)

    # Align properly
    X = features.iloc[:-1]
    y = labels.loc[X.index]

    # Drop NaNs (important)
    X = X.dropna()
    y = y.loc[X.index]

    if len(X) == 0:
        continue

    all_X.append(X)
    all_y.append(y)

# Combine all symbols
import pandas as pd

X_final = pd.concat(all_X)
y_final = pd.concat(all_y)

X_final = X_final.reset_index(drop=True)
y_final = y_final.reset_index(drop=True)

model = MLModel()
model.train(X_final, y_final)

ml_filter = MLSignalFilter(model)


# ------------------------
# 4. RUN BACKTEST
# ------------------------
runner = BacktestRunner(
    MovingAverageCrossStrategy,
    # strategy_params={
    #     "ml_filter": ml_filter,
    #     "feature_pipeline": feature_pipeline
    # }
    strategy_params={}
)

equity = runner.run(test_data)


# ------------------------
# 5. PERFORMANCE REPORT
# ------------------------
report = PerformanceReport(equity)
results = report.generate()

print("\n=== PERFORMANCE REPORT ===")
for k, v in results.items():
    print(f"{k}: {v:.4f}")


# ------------------------
# 6. TO VISUALIZE
# ------------------------
import matplotlib.pyplot as plt

equity.plot(title="Strategy Equity Curve")
plt.xlabel("Time")
plt.ylabel("Portfolio Value")
plt.grid()
plt.savefig("equity_curve.png")
plt.show()



benchmark = test_data.groupby("datetime")["close"].mean()
benchmark = benchmark / benchmark.iloc[0] * equity.iloc[0]
plt.figure()
equity.plot(label="Strategy")
benchmark.plot(label="Benchmark (Buy & Hold)")
plt.legend()
plt.title("Strategy vs Benchmark")
plt.grid()
plt.savefig("comparison.png")
plt.show()



