from core.event import FillEvent


class SimulatedExecutionHandler:

    def __init__(self, events, commission=0.001):
        self.events = events
        self.commission = commission

    def execute_order(self, order_event):

        fill_price = self._get_market_price(order_event)

        cost = fill_price * order_event.quantity
        commission = cost * self.commission

        fill = FillEvent(
            timestamp=order_event.timestamp,
            symbol=order_event.symbol,
            quantity=order_event.quantity,
            direction=order_event.direction,
            fill_price=fill_price,
            commission=commission
        )

        self.events.put(fill)

    def _get_market_price(self, order_event):
        # Placeholder (we'll improve later)
        return 100.0