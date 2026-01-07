from pathlib import Path

from models.customer_orders.order_row import OrderRow
from pipeline.utils.file_readers import ensure_file_exists, read_parquet_or_fail


def extract_order_rows_from_parquet(order_rows_parquet_path: Path) -> list[OrderRow]:
    ensure_file_exists(order_rows_parquet_path)
    order_rows: list[dict[str, str]] = read_parquet_or_fail(order_rows_parquet_path)
    return [OrderRow.model_validate(order_row) for order_row in order_rows]