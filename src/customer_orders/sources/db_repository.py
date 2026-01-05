from __future__ import annotations

from typing import TypeVar, Type
import pandas as pd
from sqlalchemy import Engine
from pydantic import BaseModel

from models.customer_orders.currency_exchange import CurrencyExchange
from models.customer_orders.customer import Customer
from models.customer_orders.order import Order

T = TypeVar("T", bound=BaseModel)


def load_db_table(engine: Engine, table: str, model: Type[T]) -> list[T]:
    df = pd.read_sql(f"SELECT * FROM [dbo].[{table}]", engine)
    records = df.to_dict(orient="records")
    return [model.model_validate(row) for row in records]


def get_customers(engine: Engine) -> list[Customer]:
    return load_db_table(engine, "Customer", Customer)


def get_orders(engine: Engine) -> list[Order]:
    return load_db_table(engine, "Orders", Order)


def get_currency_exchanges(engine: Engine) -> list[CurrencyExchange]:
    return load_db_table(engine, "CurrencyExchange", CurrencyExchange)
