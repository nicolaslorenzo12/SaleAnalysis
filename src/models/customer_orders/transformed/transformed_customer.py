from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class TransformedCustomer:
    CustomerKey: int
    Gender: Optional[str] = None
    FullName: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    Country: Optional[str] = None
    Birthday: Optional[date] = None
