from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class StagedOrderRow:
    OrderKey: int
    LineNumber: int
    ProductKey: int
    CustomerKey: int
    StoreKey: int
    Quantity: int
    UnitPrice: Decimal
    NetPrice: Decimal
    UnitCost: Decimal
    OrderDate: date
    CurrencyCode: str
    ExchangeToUsd: Decimal
