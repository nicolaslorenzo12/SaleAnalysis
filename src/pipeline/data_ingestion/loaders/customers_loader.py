from __future__ import annotations
from sqlalchemy import Engine, text

from models.orders_DW.transformed.transformed_customer import TransformedCustomer
from pipeline.data_ingestion.loaders.shared.rows_loader import load_table

DM_CUSTOMER_TABLE = "dbo.dm_customer"

def load_customers(
    dw_engine: Engine,
    customers_to_load: list[TransformedCustomer],
    *,
    truncate: bool = True,
    batch_size: int = 5000,
) -> None:
    insert_sql = text(f"""
        INSERT INTO {DM_CUSTOMER_TABLE}
        (
            CustomerKey, Gender, FullName, City,
            State, StateCode,Country, CountryCode,Birthday
        )
        VALUES
        (
            :CustomerKey, :Gender, :FullName, :City,
            :State, :StateCode ,:Country, :CountryCode , :Birthday
        )
    """)

    load_table(
        engine=dw_engine,
        table_name=DM_CUSTOMER_TABLE,
        insert_sql=insert_sql,
        items=customers_to_load,
        truncate=truncate,
        batch_size=batch_size,
    )