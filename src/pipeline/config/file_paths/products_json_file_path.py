from pathlib import Path
import os


def get_customer_orders_products_json_path() -> Path:
    return Path(os.getenv("PRODUCTS_JSON_PATH"))