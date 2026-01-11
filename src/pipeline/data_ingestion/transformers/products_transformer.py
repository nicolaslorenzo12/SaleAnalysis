from __future__ import annotations

from models.customer_orders.raw.raw_product import RawProduct
from models.customer_orders.transformed.transformed_product import TransformedProduct


def transform_products(raw_products: list[RawProduct]) -> list[TransformedProduct]:
    return [
        TransformedProduct(
            ProductKey=raw_product.ProductKey,
            ProductName=raw_product.ProductName,
            Brand=raw_product.Brand,
            Color=raw_product.Color,
            CategoryKey=raw_product.CategoryKey,
            CategoryName=raw_product.CategoryName,
            SubCategoryKey=raw_product.SubCategoryKey,
            SubCategoryName=raw_product.SubCategoryName
        )
        for raw_product in raw_products
    ]