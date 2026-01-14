from pathlib import Path
import os


def get_order_rows_parquet_path() -> Path:
    return Path(os.getenv("ORDER_ROWS_PARQUET_PATH"))