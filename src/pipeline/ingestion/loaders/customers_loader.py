from __future__ import annotations

from typing import List

from sqlalchemy import Engine, text

from models.customer_orders.transformed.transformed_customer import TransformedCustomer


def batched_dicts(
    items: List[TransformedCustomer],
    batch_size: int,
) -> List[List[dict]]:

    batches: List[List[dict]] = []

    for i in range(0, len(items), batch_size):
        batch = items[i : i + batch_size]
        batches.append([c.model_dump() for c in batch])

    return batches


def load_customers(
    dw_engine: Engine,
    customers: List[TransformedCustomer],
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

        batches = batched_dicts(customers, batch_size)

        for rows in batches:
            conn.execute(insert_sql, rows)
