from pathlib import Path

from models.customer_orders.raw.raw_order_row import RawOrderRow
from pipeline.utils.file_readers import ensure_file_exists, read_parquet_or_fail


def extract_raw_order_rows_from_parquet(order_rows_parquet_path: Path) -> list[RawOrderRow]:
    ensure_file_exists(order_rows_parquet_path)
    raw_order_rows: list[dict[str, str]] = read_parquet_or_fail(order_rows_parquet_path)
    return [RawOrderRow.model_validate(raw_order_row) for raw_order_row in raw_order_rows]