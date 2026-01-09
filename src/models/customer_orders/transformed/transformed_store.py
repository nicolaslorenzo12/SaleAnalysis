from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class TransformedStore:
    StoreKey: int
    State: str
    Country: str