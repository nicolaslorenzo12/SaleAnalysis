from pydantic import BaseModel
from decimal import Decimal


class RawOrderRow(BaseModel):
    OrderKey: int
    LineNumber: int
    ProductKey: int
    Quantity: int
    UnitPrice: Decimal
    NetPrice: Decimal
    UnitCost: Decimal
