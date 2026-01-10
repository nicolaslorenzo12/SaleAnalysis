from __future__ import annotations

from dataclasses import asdict
from typing import Iterator, Any

from sqlalchemy import Engine, text

from models.customer_orders.transformed.transformed_date import TransformedDate

DM_DATE_TABLE = "dbo.dm_date"


def batched_dicts(
    items: list[TransformedDate],
    batch_size: int,
) -> Iterator[list[dict[str, Any]]]:
    for i in range(0, len(items), batch_size):
        yield [asdict(c) for c in items[i : i + batch_size]]


def load_dates(
    dw_engine: Engine,
    customers: list[TransformedDate],
    *,
    truncate: bool = True,
    batch_size: int = 5000,
) -> None:
    insert_sql = text(f"""
        INSERT INTO {DM_DATE_TABLE}
        (
            DateKey, Date, Year, Quarter, Month,
            MonthNumber, DayofWeek, DayofWeekNumber,
            IsItAWorkingDay
        )
        VALUES
        (
            :DateKey, :Date, :Year, :Quarter,
            :Month, :MonthNumber ,:DayofWeek, :DayofWeekNumber,
             :IsItAWorkingDay
        )
    """)

    with dw_engine.begin() as conn:
        if truncate:
            conn.execute(text(f"TRUNCATE TABLE {DM_DATE_TABLE};"))

        for rows in batched_dicts(customers, batch_size):
            conn.execute(insert_sql, rows)