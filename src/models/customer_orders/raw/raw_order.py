from datetime import date
from typing import Optional

from pydantic import BaseModel


class RawOrder(BaseModel):
    OrderKey: int
    CustomerKey: int
    StoreKey: int

    OrderDate: date
    DeliveryDate: date

    CurrencyCode: str

    model_config = {
        "from_attributes": True,
    }
