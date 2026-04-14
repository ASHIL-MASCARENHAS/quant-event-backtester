import numpy as np
import pandas as pd


class PerformanceMetrics:

    @staticmethod
    def returns(equity: pd.Series):
        return equity.pct_change().dropna()

    @staticmethod
    def cumulative_returns(returns: pd.Series):
        return (1 + returns).cumprod()

    @staticmethod
    def sharpe_ratio(returns: pd.Series, risk_free_rate=0.0):

        excess = returns - risk_free_rate / 252

        return np.sqrt(252) * excess.mean() / excess.std()

    @staticmethod
    def sortino_ratio(returns: pd.Series, risk_free_rate=0.0):

        downside = returns[returns < 0]

        if len(downside) == 0:
            return np.nan

        return np.sqrt(252) * returns.mean() / downside.std()

    @staticmethod
    def volatility(returns: pd.Series):
        return np.sqrt(252) * returns.std()

    @staticmethod
    def max_drawdown(equity: pd.Series):

        peak = equity.cummax()
        drawdown = (equity - peak) / peak

        return drawdown.min()