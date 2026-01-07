from pathlib import Path

from dotenv import load_dotenv

from pipeline.extract import extract_data
load_dotenv()
import os

STORES_PATH = Path(os.environ["CUSTOMER_ORDERS_STORES_CSV_PATH"])
PRODUCTS_PATH = Path(os.environ["PRODUCTS_JSON_PATH"])
ORDER_ROWS_PATH = Path(os.environ["ORDER_ROWS_PARQUET_PATH"])

from sqlalchemy import Engine
from pipeline.loaders.customer_orders.sources.customer_orders_db_engine import get_engine


def run_pipeline() -> None:
    engine:Engine = get_engine()

    extracted_data = extract_data(engine, STORES_PATH, PRODUCTS_PATH, ORDER_ROWS_PATH)

    for customer in extracted_data.customers[:5]:
        print(customer)

    for order in extracted_data.orders[:5]:
        print(order)

    for currency_exchange in extracted_data.currency_exchanges[:5]:
        print(currency_exchange)

    for store in extracted_data.stores[:5]:
        print(store)

    for product in extracted_data.products[:5]:
        print(product)

    for order_row in extracted_data.order_rows[:5]:
        print(order_row)


if __name__ == "__main__":
    run_pipeline()
