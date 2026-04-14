import pandas as pd
from queue import Queue

from core import event
from core.engine import BacktestEngine
from data_handler.historic_csv import HistoricCSVDataHandler
from portfolio.portfolio import BasicPortfolio
from execution.simulated_execution import SimulatedExecutionHandler


class BacktestRunner:

    def __init__(self, strategy_cls, strategy_params=None):

        self.strategy_cls = strategy_cls
        self.strategy_params = strategy_params or {}

    def run(self, data):

        events = Queue()

        data_handler = HistoricCSVDataHandler(events, data)

        strategy = self.strategy_cls(
            data_handler,
            events,
            **self.strategy_params
        )

        portfolio = BasicPortfolio(events)
        execution = SimulatedExecutionHandler(events)

        engine = BacktestEngine(
            data_handler,
            strategy,
            portfolio,
            execution,
            events
        )

        engine.run()

        # Convert equity curve
        equity_df = pd.DataFrame(portfolio.equity_curve)
        if len(portfolio.equity_curve) == 0:
            raise ValueError("Equity curve is empty — check event flow.")

        equity_df.set_index("timestamp", inplace=True)

        return equity_df["equity"]