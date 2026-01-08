from __future__ import annotations

from itertools import islice
from typing import Iterable, Iterator, List

from sqlalchemy import Engine, text

from models.customer_orders.normalized.normalized_customer import NormalizedCustomer


def _batched_dicts(items: Iterable[NormalizedCustomer], batch_size: int) -> Iterator[List[dict]]:
    it = iter(items)
    while True:
        chunk = list(islice(it, batch_size))
        if not chunk:
            return
        yield [c.model_dump() for c in chunk]


def load_stg_customers(
    dw_engine: Engine,
    customers: Iterable[NormalizedCustomer],
    *,
    truncate: bool = True,
    batch_size: int = 1000,
) -> None:
    insert_sql = text("""
        INSERT INTO dbo.stg_customer
        (
            CustomerKey, Gender, FullName, City,
            StateCode, StateName, CountryCode, CountryName, Birthday
        )
        VALUES
        (
            :CustomerKey, :Gender, :FullName, :City,
            :StateCode, :StateName, :CountryCode, :CountryName, :Birthday
        )
    """)

    with dw_engine.begin() as conn:
        if truncate:
            conn.execute(text("TRUNCATE TABLE dbo.stg_customer;"))

        for rows in _batched_dicts(customers, batch_size):
            conn.execute(insert_sql, rows)
