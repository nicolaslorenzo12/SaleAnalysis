import csv
import json
from pathlib import Path
from typing import Iterator

import pyarrow.parquet as pq

from models.errors.files import FileReadError


def _ensure_file_exists(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")


def read_csv_or_fail(path: Path) -> list[dict[str, str]]:
    _ensure_file_exists(path)
    try:
        with path.open(newline="", encoding="utf-8-sig") as f:
            reader: Iterator[dict[str, str]] = csv.DictReader(f)
            return list(reader)
    except Exception as exc:
        raise FileReadError(f"Failed to read CSV file: {path}") from exc


def read_json_or_fail(path: Path) -> list[dict[str, str]]:
    _ensure_file_exists(path)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise FileReadError(f"Failed to read JSON file: {path}") from exc


def read_parquet_or_fail(path: Path) -> list[dict[str, str]]:
    _ensure_file_exists(path)
    try:
        table = pq.read_table(path)
        return table.to_pylist()
    except Exception as exc:
        raise FileReadError(f"Failed to read Parquet file: {path}") from exc
