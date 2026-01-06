from __future__ import annotations
from typing import Any, TypeVar, Type

import pandas as pd
from sqlalchemy import Engine
from pydantic import BaseModel, ValidationError

from models.customer_orders.currency_exchange import CurrencyExchange
from models.customer_orders.customer import Customer
from models.customer_orders.order import Order
from pipeline.validation.row_validation import validate_rows_with_optional_cleanup

T = TypeVar("T", bound=BaseModel)

def load_db_table(engine: Engine, table: str, model: Type[T]) -> list[T]:
    df = pd.read_sql(f"SELECT * FROM [dbo].[{table}]", engine)
    rows = df.to_dict(orient="records")
    return validate_rows_with_optional_cleanup(rows, model)


def get_customers(engine: Engine) -> list[Customer]:
    return load_db_table(engine, "Customer", Customer)


def get_orders(engine: Engine) -> list[Order]:
    return load_db_table(engine, "Orders", Order)


def get_currency_exchanges(engine: Engine) -> list[CurrencyExchange]:
    return load_db_table(engine, "CurrencyExchange", CurrencyExchange)
