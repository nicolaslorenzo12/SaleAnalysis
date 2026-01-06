from pathlib import Path

import pandas as pd

from models.errors.files import FileReadError


def ensure_file_exists(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

def read_csv_or_fail(path: Path, *, encoding: str = "utf-8-sig") -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding=encoding)
    except Exception as exc:
        raise FileReadError(
            f"Failed to read CSV file: {path}"
        ) from exc