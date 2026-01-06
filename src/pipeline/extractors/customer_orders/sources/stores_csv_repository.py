from pathlib import Path
from pipeline.validation.filesystem import ensure_file_exists, read_csv_or_fail
from models.customer_orders.store import Store


def load_stores_from_csv(path: Path) -> list[Store]:
    ensure_file_exists(path)
    df = read_csv_or_fail(path)
    rows = df.to_dict(orient="records")

    return [Store.model_validate(row) for row in rows]