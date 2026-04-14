from collections import defaultdict
from core.event import OrderEvent


class BasicPortfolio:

    def __init__(self, events, initial_capital=100000):

        self.events = events
        self.initial_capital = initial_capital
        self.cash = initial_capital

        self.positions = defaultdict(lambda: 0)
        self.holdings = defaultdict(lambda: 0.0)

        self.current_prices = {}

        self.trade_log = []

        self.equity_curve = []

    def update_signal(self, event):

        symbol = event.symbol

        # Basic position sizing (can be replaced later)
        quantity = 100

        order = self.generate_order(event, quantity)

        if order:
            self.events.put(order)

    def generate_order(self, signal_event, quantity):

        direction = None

        if signal_event.signal_type == "LONG":
            direction = "BUY"
        elif signal_event.signal_type == "SHORT":
            direction = "SELL"
        elif signal_event.signal_type == "EXIT":
            direction = "SELL"

        if direction is None:
            return None

        return OrderEvent(
            timestamp=signal_event.timestamp,
            symbol=signal_event.symbol,
            order_type="MKT",
            quantity=quantity,
            direction=direction
        )

    def update_fill(self, event):

        symbol = event.symbol
        fill_cost = event.fill_price * event.quantity

        if event.direction == "BUY":
            self.positions[symbol] += event.quantity
            self.cash -= fill_cost

        elif event.direction == "SELL":
            self.positions[symbol] -= event.quantity
            self.cash += fill_cost

        # Log trade
        self.trade_log.append({
            "timestamp": event.timestamp,
            "symbol": symbol,
            "quantity": event.quantity,
            "price": event.fill_price,
            "direction": event.direction
        })

    def update_market_value(self, market_event):

        print(">>> PORTFOLIO: updating equity")

        symbol = market_event.symbol
        price = market_event.data["close"]

        self.current_prices[symbol] = price

        total_value = self.cash

        for sym, qty in self.positions.items():
            if sym in self.current_prices:
                total_value += qty * self.current_prices[sym]

        self.equity_curve.append({
            "timestamp": market_event.timestamp,
            "equity": total_value
        })