from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class TransformedOrderRow:
    OrderKey: int
    LineNumber: int
    ProductKey: int
    CustomerKey: int
    StoreKey: int
    Quantity: int
    OrderDate: date
    UnitPriceInUSD: Decimal
    NetPriceInUSD: Decimal
    UnitCostInUSD: Decimal