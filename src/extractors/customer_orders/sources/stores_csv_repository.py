from pathlib import Path

import pandas as pd

from file_io.filesystem import ensure_file_exists
from models.customer_orders.store import Store
from models.errors.files import FileReadError


def get_stores_from_csv(path: Path) -> list[Store]:

    ensure_file_exists(path)

    try:
        stores_df = pd.read_csv(
            path,
            encoding="utf-8-sig",
        )
    except Exception as exc:
        raise FileReadError(
            f"Failed to read stores CSV file: {path}"
        ) from exc

    return [Store.model_validate(store) for store in stores_df.to_dict(orient="records")]

