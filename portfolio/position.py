class Position:

    def __init__(self, symbol):
        self.symbol = symbol
        self.quantity = 0
        self.avg_price = 0.0

    def update(self, quantity, price):

        if self.quantity + quantity == 0:
            self.quantity = 0
            self.avg_price = 0.0
            return

        new_total = self.quantity + quantity

        self.avg_price = (
            (self.quantity * self.avg_price) + (quantity * price)
        ) / new_total

        self.quantity = new_total