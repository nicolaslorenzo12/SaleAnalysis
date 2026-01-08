from typing import Optional

from pydantic import BaseModel
from decimal import Decimal


class RawOrderRow(BaseModel):
    OrderKey: int
    LineNumber: int
    ProductKey: Optional[int] = None
    Quantity: Optional[int] = None
    UnitPrice: Optional[Decimal] = None
    NetPrice: Optional[Decimal] = None
    UnitCost: Optional[Decimal] = None
