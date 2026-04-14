import pandas as pd


class BuyAndHoldBenchmark:

    def __init__(self, initial_capital=100000):
        self.initial_capital = initial_capital

    def run(self, df: pd.DataFrame):

        # Assume single asset for simplicity
        symbol = df["symbol"].iloc[0]

        prices = df[df["symbol"] == symbol]["close"]

        returns = prices.pct_change().fillna(0)

        equity = (1 + returns).cumprod() * self.initial_capital

        return equity