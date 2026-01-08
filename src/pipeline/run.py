from dotenv import load_dotenv
import os

from pathlib import Path
from pipeline.infrastructure.databases.customer_orders_engine import get_customer_orders_engine
from pipeline.infrastructure.databases.orders_dw_engine import get_orders_dw_engine
from pipeline.ingestion.ingestion import ingest_data

STORES_PATH = Path(os.environ["CUSTOMER_ORDERS_STORES_CSV_PATH"])
PRODUCTS_PATH = Path(os.environ["PRODUCTS_JSON_PATH"])
ORDER_ROWS_PATH = Path(os.environ["ORDER_ROWS_PARQUET_PATH"])

from sqlalchemy import Engine


def run_pipeline() -> None:

    customer_orders_engine:Engine = get_customer_orders_engine()
    orders_dw_engine:Engine = get_orders_dw_engine()

    ingest_data(customer_orders_engine, orders_dw_engine,STORES_PATH, PRODUCTS_PATH, ORDER_ROWS_PATH)

if __name__ == "__main__":
    load_dotenv()
    run_pipeline()
