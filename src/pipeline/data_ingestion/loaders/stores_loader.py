from __future__ import annotations
from typing import List
from sqlalchemy import Engine, text
from models.customer_orders.transformed.transformed_store import TransformedStore
from pipeline.data_ingestion.loaders.shared.rows_loader import load_table

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

    load_table(
        engine=dw_engine,
        table_name=DM_STORE_TABLE,
        insert_sql=insert_sql,
        items=stores_to_load,
        truncate=truncate,
        batch_size=None,
    )
