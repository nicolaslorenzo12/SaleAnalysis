from __future__ import annotations
from sqlalchemy import Engine, text

from models.orders_DW.transformed.tranformed_order_row import TransformedOrderRow
from pipeline.data_ingestion.loaders.shared.rows_loader import load_table
DM_ORDER_ROW_TABLE = "dbo.dm_order_row"

def load_order_rows(
    dw_engine: Engine,
    order_rows_to_load: list[TransformedOrderRow],
    *,
    truncate: bool = True,
    batch_size: int = 10000,
) -> None:
    insert_sql = text(f"""
        INSERT INTO {DM_ORDER_ROW_TABLE}
        (
            OrderKey, LineNumber, ProductKey, CustomerKey, StoreKey,
            Quantity, OrderDate, UnitPriceInUSD, NetPriceInUSD,
            UnitCostInUSD
        )
        VALUES
        (
            :OrderKey, :LineNumber, :ProductKey, :CustomerKey,
            :StoreKey, :Quantity ,:OrderDate, :UnitPriceInUSD,
             :NetPriceInUSD, :UnitCostInUSD
        )
    """)

    load_table(
        engine=dw_engine,
        table_name=DM_ORDER_ROW_TABLE,
        insert_sql=insert_sql,
        items=order_rows_to_load,
        truncate=truncate,
        batch_size=batch_size,
    )