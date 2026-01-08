import sqlalchemy
from sqlalchemy import Engine, text

from models.raw.raw_customer import RawCustomer


def extract_raw_customers(engine: Engine) -> list[RawCustomer]:
    with engine.connect() as conn:
        raw_customers: list[sqlalchemy.engine.RowMapping] = conn.execute(text("SELECT * FROM [dbo].[Customer]")).mappings().all()
    return [RawCustomer.model_validate(dict(raw_customer)) for raw_customer in raw_customers]
