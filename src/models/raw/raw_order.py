from datetime import date
from typing import Optional

from pydantic import BaseModel


class RawOrder(BaseModel):
    OrderKey: int
    CustomerKey: Optional[int] = None
    StoreKey: Optional[int] = None

    OrderDate: Optional[date] = None
    DeliveryDate: Optional[date] = None

    CurrencyCode: Optional[str] = None

    model_config = {
        "from_attributes": True,
    }
