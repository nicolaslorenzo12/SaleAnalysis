from pathlib import Path

from models.customer_orders.product import Product
from pipeline.utils.file_readers import ensure_file_exists, read_json_or_fail


def extract_products_from_json(products_json_path: Path) -> list[Product]:
    ensure_file_exists(products_json_path)
    products: list[dict[str, str]] = read_json_or_fail(products_json_path)
    return [Product.model_validate(product) for product in products]