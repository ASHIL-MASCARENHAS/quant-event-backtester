from abc import ABC, abstractmethod

class Portfolio(ABC):
    """
    Responsible for:
    - Position tracking
    - PnL calculation
    - Order generation
    """

    @abstractmethod
    def update_signal(self, event):
        pass

    @abstractmethod
    def update_fill(self, event):
        pass

    @abstractmethod
    def generate_order(self, signal_event):
        pass