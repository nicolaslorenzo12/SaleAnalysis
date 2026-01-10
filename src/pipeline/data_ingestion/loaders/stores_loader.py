from __future__ import annotations

from dataclasses import asdict
from typing import List

from sqlalchemy import Engine, text

from models.customer_orders.transformed.transformed_store import TransformedStore

DM_STORE_TABLE = "dbo.dm_store"


def load_stores(
    dw_engine: Engine,
    stores_to_load: List[TransformedStore],
    *,
    truncate: bool = True,
) -> None:

    insert_sql = text(f"""
        INSERT INTO {DM_STORE_TABLE}
        (
            StoreKey, State, Country, CountryCode
        )
        VALUES
        (
            :StoreKey, :State, :Country, :CountryCode
        )
    """)

    with dw_engine.begin() as conn:
        if truncate:
            conn.execute(text(f"TRUNCATE TABLE {DM_STORE_TABLE};"))

        for rows in stores_to_load:
            conn.execute(insert_sql, asdict(rows))
