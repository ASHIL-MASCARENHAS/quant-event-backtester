import pandas as pd
from collections import defaultdict
from core.event import SignalEvent
from .base import Strategy
from core.event import MarketEvent, SignalEvent, OrderEvent, FillEvent


class MovingAverageCrossStrategy(Strategy):

    def __init__(self, data_handler, events,
             short_window = 5, long_window = 10,
             ml_filter=None, feature_pipeline=None):

        super().__init__(data_handler, events)

        self.short_window = short_window
        self.long_window = long_window

        self.ml_filter = ml_filter
        self.feature_pipeline = feature_pipeline

        self.symbols = data_handler.get_all_symbols()

        self.bought = {symbol: False for symbol in self.symbols}

    def generate_signals(self, event):
        if event.__class__.__name__ != "MarketEvent":
            return

        symbol = event.symbol

        bars = self.data_handler.get_latest_data(
            symbol,
            N=self.long_window
        )

        if len(bars) < self.long_window:
            return

        close_prices = bars["close"]

        short_ma = close_prices.rolling(self.short_window).mean().iloc[-1]
        long_ma = close_prices.rolling(self.long_window).mean().iloc[-1]

        timestamp = bars.index[-1]

        # Generate signals
        if short_ma > long_ma and not self.bought[symbol]:

            signal = SignalEvent(timestamp, symbol, "LONG", 1.0)
            self._emit_signal(signal, bars)
            self.bought[symbol] = True

        elif short_ma < long_ma and self.bought[symbol]:

            signal = SignalEvent(timestamp, symbol, "EXIT", 1.0)
            self._emit_signal(signal, bars)
            self.bought[symbol] = False

    def _emit_signal(self, signal, bars):
        if self.ml_filter and self.feature_pipeline:

            features = self.feature_pipeline.transform(bars)

            if len(features) == 0:
                return

            filtered_signal = self.ml_filter.filter(features, signal)

            if filtered_signal:
                self.events.put(filtered_signal)

        else:
            self.events.put(signal)