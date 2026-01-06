from __future__ import annotations

from typing import TypeVar, Type
import pandas as pd
from sqlalchemy import Engine
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError

from models.customer_orders.currency_exchange import CurrencyExchange
from models.customer_orders.customer import Customer
from models.customer_orders.order import Order
from models.errors.db import TableError

T = TypeVar("T", bound=BaseModel)


def _load_db_table(engine: Engine, table: str, model: Type[T]) -> list[T]:
    try:
        df = pd.read_sql(f"SELECT * FROM [dbo].[{table}]", engine)
    except SQLAlchemyError as exc:
        raise TableError(
            f"Failed to load table '{table}' from database"
        ) from exc

    return [model.model_validate(row) for row in df.to_dict(orient="records")]

def get_customers(engine: Engine) -> list[Customer]:
    return _load_db_table(engine, "Customer", Customer)


def get_orders(engine: Engine) -> list[Order]:
    return _load_db_table(engine, "Orders", Order)


def get_currency_exchanges(engine: Engine) -> list[CurrencyExchange]:
    return _load_db_table(engine, "CurrencyExchange", CurrencyExchange)
