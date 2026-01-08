import sqlalchemy
from sqlalchemy import Engine, text

from models.raw.raw_order import RawOrder


def extract_raw_orders(engine: Engine) -> list[RawOrder]:
    with engine.connect() as conn:
        raw_orders: list[sqlalchemy.engine.RowMapping] = conn.execute(text("SELECT * FROM [dbo].[Orders]")).mappings().all()
    return [RawOrder.model_validate(dict(raw_order)) for raw_order in raw_orders]