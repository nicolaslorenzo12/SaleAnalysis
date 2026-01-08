from pathlib import Path
from pipeline.utils.file_readers import ensure_file_exists, read_csv_or_fail
from models.raw.raw_store import RawStore


def extract_raw_stores_from_csv(stores_csv_path: Path) -> list[RawStore]:
    ensure_file_exists(stores_csv_path)
    raw_stores: list[dict[str, str]] = read_csv_or_fail(stores_csv_path)
    return [RawStore.model_validate(raw_store) for raw_store in raw_stores]