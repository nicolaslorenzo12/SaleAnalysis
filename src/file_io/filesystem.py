from pathlib import Path

def ensure_file_exists(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
