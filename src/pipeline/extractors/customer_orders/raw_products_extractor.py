from pathlib import Path

from models.raw.raw_product import RawProduct
from pipeline.utils.file_readers import ensure_file_exists, read_json_or_fail


def extract_raw_products_from_json(products_json_path: Path) -> list[RawProduct]:
    ensure_file_exists(products_json_path)
    raw_products: list[dict[str, str]] = read_json_or_fail(products_json_path)
    return [RawProduct.model_validate(raw_product) for raw_product in raw_products]