from datetime import date
from pydantic import BaseModel, Field


class Order(BaseModel):
    OrderKey: int = Field(..., ge=1)
    CustomerKey: int = Field(..., ge=1)
    StoreKey: int = Field(..., ge=1)

    OrderDate: date
    DeliveryDate: date

    CurrencyCode: str = Field(..., max_length=5)

    model_config = {
        "from_attributes": True,
        "extra": "forbid",
        "validate_assignment": True,
    }
