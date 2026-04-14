import pandas as pd
import numpy as np

np.random.seed(42)

def generate_symbol_data(symbol, start_price=100, days=300):

    dates = pd.date_range(start="2020-01-01", periods=days, freq="D")

    prices = [start_price]

    for _ in range(days - 1):
        change = np.random.normal(0, 0.01)
        prices.append(prices[-1] * (1 + change))

    prices = np.array(prices)

    df = pd.DataFrame({
        "datetime": dates,
        "symbol": symbol,
        "open": prices,
        "high": prices * (1 + np.random.uniform(0, 0.01, days)),
        "low": prices * (1 - np.random.uniform(0, 0.01, days)),
        "close": prices,
        "volume": np.random.randint(100, 1000, days)
    })

    return df


def main():

    symbols = ["AAPL", "MSFT"]

    data = pd.concat([
        generate_symbol_data(symbol) for symbol in symbols
    ])

    data.to_csv("data/raw/market_data.csv", index=False)

    print("✅ Data generated at data/raw/market_data.csv")


if __name__ == "__main__":
    main()