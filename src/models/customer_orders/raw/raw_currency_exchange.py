from datetime import date
from pydantic import BaseModel


class RawCurrencyExchange(BaseModel):
    Date: date

    FromCurrency: str
    ToCurrency: str

    Exchange: float

    model_config = {
        "from_attributes": True,
    }
