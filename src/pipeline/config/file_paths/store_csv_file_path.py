from pathlib import Path
import os

def get_customer_orders_stores_csv_path() -> Path:
    return Path(os.getenv("CUSTOMER_ORDERS_STORES_CSV_PATH"))