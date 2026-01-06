from datetime import date
from pydantic import BaseModel, Field


class CurrencyExchange(BaseModel):
    Date: date

    FromCurrency: str
    ToCurrency: str

    Exchange: float

    model_config = {
        "from_attributes": True,
    }
