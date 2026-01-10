from pathlib import Path
from pipeline.utils.file_readers import read_csv_or_fail
from models.customer_orders.raw.raw_store import RawStore


def extract_raw_stores_from_csv(stores_csv_path: Path) -> list[RawStore]:
    raw_stores: list[dict[str, str]] = read_csv_or_fail(stores_csv_path)
    return [RawStore.model_validate(raw_store) for raw_store in raw_stores]