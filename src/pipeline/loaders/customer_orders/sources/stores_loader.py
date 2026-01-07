from pathlib import Path
from pipeline.validation.filesystem import ensure_file_exists, read_csv_or_fail
from models.customer_orders.store import Store


def load_stores_from_csv(stores_csv_path: Path) -> list[Store]:
    ensure_file_exists(stores_csv_path)
    stores: list[dict[str, str]] = read_csv_or_fail(stores_csv_path)
    return [Store.model_validate(store) for store in stores]