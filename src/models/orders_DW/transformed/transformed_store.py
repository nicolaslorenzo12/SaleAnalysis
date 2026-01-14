from dataclasses import dataclass
from typing import Optional


@dataclass
class TransformedStore:
    StoreKey: int
    State: Optional[str] = None
    Country: Optional[str] = None
    CountryCode: Optional[str] = None