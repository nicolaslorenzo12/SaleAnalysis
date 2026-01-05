from datetime import date
from pydantic import BaseModel, Field


class CurrencyExchange(BaseModel):
    Date: date

    FromCurrency: str = Field(..., min_length=3, max_length=3)
    ToCurrency: str = Field(..., min_length=3, max_length=3)

    Exchange: float

    model_config = {
        "from_attributes": True,
        "extra": "forbid",
        "validate_assignment": True,
    }
