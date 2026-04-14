from abc import ABC
from dataclasses import dataclass
from datetime import datetime

class Event(ABC):
    """Base class for all events."""
    pass


@dataclass
class MarketEvent(Event):
    timestamp: datetime
    symbol: str
    data: dict


@dataclass
class SignalEvent(Event):
    timestamp: datetime
    symbol: str
    signal_type: str  # 'LONG', 'SHORT', 'EXIT'
    strength: float


@dataclass
class OrderEvent(Event):
    timestamp: datetime
    symbol: str
    order_type: str  # 'MKT', 'LMT'
    quantity: int
    direction: str   # 'BUY', 'SELL'


@dataclass
class FillEvent(Event):
    timestamp: datetime
    symbol: str
    quantity: int
    direction: str
    fill_price: float
    commission: float