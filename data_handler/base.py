from abc import ABC, abstractmethod

class DataHandler(ABC):
    """
    Responsible for:
    - Providing market data
    - Avoiding lookahead bias
    """

    @abstractmethod
    def get_latest_data(self, symbol: str, N: int = 1):
        pass

    @abstractmethod
    def update_bars(self):
        """
        Push next market event into the system
        """
        pass

    @abstractmethod
    def get_all_symbols(self):
        pass