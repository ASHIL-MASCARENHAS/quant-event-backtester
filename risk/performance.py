from .metrics import PerformanceMetrics


class PerformanceReport:

    def __init__(self, equity_curve):
        self.equity = equity_curve
        self.returns = PerformanceMetrics.returns(self.equity)

    def generate(self):

        report = {
            "Cumulative Return":
                PerformanceMetrics.cumulative_returns(self.returns).iloc[-1],

            "Sharpe Ratio":
                PerformanceMetrics.sharpe_ratio(self.returns),

            "Sortino Ratio":
                PerformanceMetrics.sortino_ratio(self.returns),

            "Volatility":
                PerformanceMetrics.volatility(self.returns),

            "Max Drawdown":
                PerformanceMetrics.max_drawdown(self.equity)
        }

        return report