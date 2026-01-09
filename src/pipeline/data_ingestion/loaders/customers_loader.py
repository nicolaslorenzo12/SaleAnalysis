from __future__ import annotations

from dataclasses import asdict
from typing import List

from sqlalchemy import Engine, text

from models.customer_orders.transformed.transformed_customer import TransformedCustomer

DM_CUSTOMER_TABLE = "dbo.dm_customer"


def batched_dicts(
    items: List[TransformedCustomer],
    batch_size: int,
) -> List[List[dict]]:
    batches: List[List[dict]] = []

    for i in range(0, len(items), batch_size):
        yield [asdict(c) for c in items[i: i + batch_size]]

    return batches


def load_customers(
    dw_engine: Engine,
    customers: List[TransformedCustomer],
    *,
    truncate: bool = True,
    batch_size: int = 5000,
) -> None:
    insert_sql = text(f"""
        INSERT INTO {DM_CUSTOMER_TABLE}
        (
            CustomerKey, Gender, FullName, City,
            State, Country, Birthday
        )
        VALUES
        (
            :CustomerKey, :Gender, :FullName, :City,
            :State,:Country, :Birthday
        )
    """)

    with dw_engine.begin() as conn:
        if truncate:
            conn.execute(text(f"TRUNCATE TABLE {DM_CUSTOMER_TABLE};"))

        for rows in batched_dicts(customers, batch_size):
            conn.execute(insert_sql, rows)
