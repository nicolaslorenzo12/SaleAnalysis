from __future__ import annotations
from typing import List
from sqlalchemy import Engine, text
from models.orders_DW.transformed.transformed_product import TransformedProduct
from pipeline.data_ingestion.loaders.shared.rows_loader import load_table

DM_PRODUCT_TABLE = "dbo.dm_product"

def load_products(
    dw_engine: Engine,
    products_to_load: List[TransformedProduct],
    *,
    truncate: bool = True,
) -> None:

    insert_sql = text(f"""
        INSERT INTO {DM_PRODUCT_TABLE}
        (
            ProductKey, ProductName, Brand, Color,
            CategoryKey, CategoryName, SubCategoryKey,
            SubCategoryName
        )
        VALUES
        (
            :ProductKey, :ProductName, :Brand, :Color,
            :CategoryKey, :CategoryName, :SubCategoryKey,
            :SubCategoryName
        )
    """)

    load_table(
        engine=dw_engine,
        table_name=DM_PRODUCT_TABLE,
        insert_sql=insert_sql,
        items=products_to_load,
        truncate=truncate,
        batch_size=None,
    )