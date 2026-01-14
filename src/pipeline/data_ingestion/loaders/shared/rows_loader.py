from __future__ import annotations

from dataclasses import asdict
from typing import Iterator, TypeVar, TypeAlias

from sqlalchemy import Engine, text

from models.orders_DW.transformed.transformed_customer import TransformedCustomer
from models.orders_DW.transformed.transformed_date import TransformedDate
from models.orders_DW.transformed.transformed_product import TransformedProduct
from models.orders_DW.transformed.transformed_store import TransformedStore

AllowedRow: TypeAlias = (
    TransformedStore
    | TransformedCustomer
    | TransformedDate
    | TransformedProduct
)

T = TypeVar("T", bound=AllowedRow)


def batched_dicts(items: list[T], batch_size: int) -> Iterator[list[dict[str, object]]]:
    for i in range(0, len(items), batch_size):
        yield [asdict(x) for x in items[i : i + batch_size]]


def load_table(
    *,
    engine: Engine,
    table_name: str,
    insert_sql: str,
    items: list[T],
    truncate: bool = True,
    batch_size: int | None = None,
) -> None:

    with engine.begin() as conn:
        if truncate:
            conn.execute(text(f"TRUNCATE TABLE {table_name};"))

        if batch_size is None:
            for item in items:
                conn.execute(insert_sql, asdict(item))
        else:
            for batch in batched_dicts(items, batch_size):
                conn.execute(insert_sql, batch)
