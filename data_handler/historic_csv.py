import pandas as pd
from collections import defaultdict
from core.event import MarketEvent
from .base import DataHandler


class HistoricCSVDataHandler(DataHandler):

    def __init__(self, events, data: pd.DataFrame):

        self.events = events
        self.data = data

        self.symbols = data["symbol"].unique()

        # Store per-symbol data
        self.symbol_data = {
            symbol: df.sort_index()
            for symbol, df in data.groupby("symbol")
        }

        # Iterators per symbol
        self.latest_index = {symbol: 0 for symbol in self.symbols}

        self.continue_backtest = True

    def get_all_symbols(self):
        return self.symbols

    def get_latest_data(self, symbol, N=1):

        df = self.symbol_data[symbol]

        idx = self.latest_index[symbol]

        if idx < N:
            return df.iloc[:idx]

        return df.iloc[idx - N:idx]

    def update_bars(self):

        bars_pushed = False

        for symbol in self.symbols:

            df = self.symbol_data[symbol]
            idx = self.latest_index[symbol]

            if idx < len(df):

                bar = df.iloc[idx]

                event = MarketEvent(
                    timestamp=bar.name,
                    symbol=symbol,
                    data=bar.to_dict()
                )

                self.events.put(event)

                self.latest_index[symbol] += 1
                bars_pushed = True

                print(f"MarketEvent: {symbol} @ {bar.name}")
                
        # Stop only if ALL symbols are exhausted
        if not bars_pushed:
            self.continue_backtest = False
