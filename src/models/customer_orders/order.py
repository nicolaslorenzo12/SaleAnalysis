from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Order(BaseModel):
    OrderKey: int
    CustomerKey: int
    StoreKey: int

    OrderDate: Optional[date] = None
    DeliveryDate: Optional[date] = None

    CurrencyCode: Optional[str] = None

    model_config = {
        "from_attributes": True,
    }
