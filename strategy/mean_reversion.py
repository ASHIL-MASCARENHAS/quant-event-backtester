import pandas as pd
from core.event import SignalEvent
from .base import Strategy


class MeanReversionStrategy(Strategy):

    def __init__(self, data_handler, events,
                 window=20, z_threshold=2.0):

        super().__init__(data_handler, events)

        self.window = window
        self.z_threshold = z_threshold

        self.symbols = data_handler.get_all_symbols()
        self.position_state = {symbol: 0 for symbol in self.symbols}
        # 0 = flat, 1 = long, -1 = short

    def generate_signals(self, event):

        if event.__class__.__name__ != "MarketEvent":
            return

        symbol = event.symbol

        bars = self.data_handler.get_latest_data(symbol, N=self.window)

        if len(bars) < self.window:
            return

        prices = bars["close"]

        mean = prices.mean()
        std = prices.std()

        if std == 0:
            return

        z_score = (prices.iloc[-1] - mean) / std

        timestamp = bars.index[-1]

        current_pos = self.position_state[symbol]

        if z_score < -self.z_threshold and current_pos == 0:

            self.events.put(SignalEvent(timestamp, symbol, "LONG", 1.0))
            self.position_state[symbol] = 1

        elif z_score > self.z_threshold and current_pos == 0:

            self.events.put(SignalEvent(timestamp, symbol, "SHORT", 1.0))
            self.position_state[symbol] = -1

        elif abs(z_score) < 0.5 and current_pos != 0:

            self.events.put(SignalEvent(timestamp, symbol, "EXIT", 1.0))
            self.position_state[symbol] = 0