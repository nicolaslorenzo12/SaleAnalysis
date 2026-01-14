from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class RawCurrencyExchange(BaseModel):
    Date: date

    FromCurrency: str
    ToCurrency: str

    Exchange: Decimal

    model_config = {
        "from_attributes": True,
    }
