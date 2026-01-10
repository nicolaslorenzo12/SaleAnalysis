import sqlalchemy
from sqlalchemy import Engine, text

from models.customer_orders.raw.raw_date import RawDate


def extract_raw_dates(engine: Engine) -> list[RawDate]:
    with engine.connect() as conn:
        raw_dates: list[sqlalchemy.engine.RowMapping] = conn.execute(text("SELECT * FROM [dbo].[Date]")).mappings().all()
    return [RawDate.model_validate(dict(raw_date)) for raw_date in raw_dates]
