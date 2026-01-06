from datetime import date
from pydantic import BaseModel, Field


class Order(BaseModel):
    OrderKey: int
    CustomerKey: int
    StoreKey: int

    OrderDate: date
    DeliveryDate: date

    CurrencyCode: str | None = None

    model_config = {
        "from_attributes": True,
        "extra": "forbid",
        "validate_assignment": True,
    }
