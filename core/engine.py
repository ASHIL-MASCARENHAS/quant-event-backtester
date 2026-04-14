from queue import Queue

from core import event
from core.event import MarketEvent

class BacktestEngine:
    """
    Orchestrates entire system
    """

    def __init__(
        self,
        data_handler,
        strategy,
        portfolio,
        execution_handler,
        events
    ):
        self.events = events

        self.data_handler = data_handler
        self.strategy = strategy
        self.portfolio = portfolio
        self.execution_handler = execution_handler

    def run(self):

        while self.data_handler.continue_backtest:

            # Step 1: Push market events
            self.data_handler.update_bars()

            # Step 2: Process queue
            while not self.events.empty():

                event = self.events.get()
                event_type = event.__class__.__name__

                if event_type == "MarketEvent":
                    print(">>> ENGINE: MarketEvent received")
                    self.portfolio.update_market_value(event)
                    self.strategy.generate_signals(event)

                elif event_type == "SignalEvent":
                    self.portfolio.update_signal(event)

                elif event_type == "OrderEvent":
                    self.execution_handler.execute_order(event)

                elif event_type == "FillEvent":
                    self.portfolio.update_fill(event)