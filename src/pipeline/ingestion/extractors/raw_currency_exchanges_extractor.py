import sqlalchemy
from sqlalchemy import Engine, text

from models.customer_orders.raw.raw_currency_exchange import RawCurrencyExchange


def extract_raw_currency_exchanges(engine: Engine) -> list[RawCurrencyExchange]:
    with engine.connect() as conn:
        raw_currency_exchanges: list[sqlalchemy.engine.RowMapping] = conn.execute(text("SELECT * FROM [dbo].[CurrencyExchange]")).mappings().all()
    return [RawCurrencyExchange.model_validate(dict(raw_currency_exchange)) for raw_currency_exchange in raw_currency_exchanges]
