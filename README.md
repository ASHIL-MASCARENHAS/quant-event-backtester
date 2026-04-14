# Event-Driven Multi-Asset Quantitative Backtesting Engine

A modular, research-grade quantitative backtesting system built from scratch to simulate, evaluate, and validate trading strategies under realistic market conditions.

---

## 📊 Results Visualization

### Strategy Equity Curve

![Equity Curve](equity_curve.png)

### Strategy vs Benchmark

![Comparison](comparison.png)

---

## 🧠 Architecture

```
Market Data → Event Queue → Strategy → Signal → Portfolio → Execution → Equity Curve → Performance Metrics
```

### Core Components

* **DataHandler** – Handles ingestion and prevents lookahead bias
* **Strategy** – Generates trading signals
* **Portfolio** – Tracks positions, cash, and PnL
* **ExecutionHandler** – Simulates order execution
* **BacktestEngine** – Orchestrates event-driven workflow

---

## ⚙️ Features

### System Design

* Event-driven architecture (queue-based)
* Modular OOP design
* Multi-asset support
* Plug-and-play components

### Data & ETL

* CSV / Parquet ingestion
* Datetime indexing & validation
* Missing data handling
* Lookahead bias prevention

### Strategy Layer

* Moving Average Crossover
* Z-score Mean Reversion
* Extensible strategy interface

### Portfolio & Execution

* Cash & position tracking
* Trade lifecycle simulation
* Transaction cost modeling
* Equity curve tracking

### Risk & Performance

* Sharpe Ratio
* Sortino Ratio
* Volatility
* Max Drawdown
* Cumulative Returns

### Validation

* Train/test split
* Out-of-sample evaluation
* Benchmark comparison

### ML Integration

* Feature engineering pipeline
* Logistic regression model
* Signal filtering layer

---

## 📈 Results & Insights

**Out-of-Sample Performance:**

* Cumulative Return: ~1.00
* Sharpe Ratio: ~0
* Max Drawdown: ~3%

**Key Insight:**

> The moving average crossover strategy exhibited near-zero Sharpe, indicating lack of alpha under tested conditions and validating the correctness and neutrality of the backtesting framework.

---

## 📂 Project Structure

```
quant_backtester/
│
├── core/
├── data_handler/
├── strategy/
├── portfolio/
├── execution/
├── risk/
├── validation/
├── ml/
├── etl/
│
├── data/
├── main.py
├── generate_data.py
└── requirements.txt
```

---

## 🚀 How to Run

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python generate_data.py
python main.py
```

---

## 🧩 Design Principles

* No lookahead bias
* Strict separation of concerns
* Modular & extensible architecture
* Reproducible experimentation

---

## 🔮 Future Work

* Walk-forward optimization
* Advanced execution models
* Position sizing (Kelly / volatility scaling)
* Real market data integration
* Hyperparameter tuning

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* scikit-learn
* Matplotlib

---

## 📌 Summary

This project demonstrates the design of a **production-grade quantitative research system**, combining software engineering best practices with financial modeling and data-driven analysis.