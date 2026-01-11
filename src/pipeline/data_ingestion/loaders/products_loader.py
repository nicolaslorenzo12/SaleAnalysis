from __future__ import annotations

from dataclasses import asdict
from typing import List

from sqlalchemy import Engine, text

from models.customer_orders.transformed.transformed_product import TransformedProduct

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

    with dw_engine.begin() as conn:
        if truncate:
            conn.execute(text(f"TRUNCATE TABLE {DM_PRODUCT_TABLE};"))

        for rows in products_to_load:
            conn.execute(insert_sql, asdict(rows))