from pathlib import Path
from sqlalchemy import Engine
from pipeline.ingestion.raw_customer_ingestion import ingest_customers


def ingest_data(customer_orders_engine: Engine, orders_dw_engine: Engine, stores_path:Path, products_path: Path, order_rows_path: Path) -> None:

    ingest_customers(customer_orders_engine, orders_dw_engine)