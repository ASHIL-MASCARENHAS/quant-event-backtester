from abc import ABC, abstractmethod

class ExecutionHandler(ABC):
    """
    Responsible for:
    - Simulating/handling order execution
    """

    @abstractmethod
    def execute_order(self, order_event):
        pass