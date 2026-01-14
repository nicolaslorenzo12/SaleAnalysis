from __future__ import annotations

import logging
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import Engine

from pipeline.config.file_paths.order_rows_parquet_file_path import get_order_rows_parquet_path
from pipeline.config.file_paths.products_json_file_path import get_customer_orders_products_json_path
from pipeline.config.file_paths.store_csv_file_path import get_customer_orders_stores_csv_path
from pipeline.data_ingestion.date_ingestion import ingest_dates
from pipeline.data_ingestion.order_rows_ingestion import ingest_order_rows
from pipeline.data_ingestion.products_ingestion import ingest_products
from pipeline.data_ingestion.stores_ingestion import ingest_stores
from pipeline.infrastructure.databases.customer_orders_engine import get_customer_orders_engine
from pipeline.infrastructure.databases.orders_dw_engine import get_orders_dw_engine
from pipeline.infrastructure.logging_config.logging import configure_logging
from pipeline.data_ingestion.customers_ingestion import ingest_customers

def run_pipeline() -> None:
    configure_logging()
    logger = logging.getLogger(__name__)

    load_dotenv()

    logger.info("Starting pipeline")

    logger.info("Creating customer orders engine")
    customer_orders_engine: Engine = get_customer_orders_engine()

    logger.info("Creating orders DW engine")
    orders_dw_engine: Engine = get_orders_dw_engine()

    logger.info("Starting customer data ingestion")
    ingest_customers(customer_orders_engine, orders_dw_engine)

    logger.info("Customers loaded successfully")

    logger.info("Starting dates ingestion")
    ingest_dates(customer_orders_engine, orders_dw_engine)
    logger.info("Dates loaded successfully")

    stores_csv_path: Path = get_customer_orders_stores_csv_path()

    logger.info("Starting stores ingestion")
    ingest_stores(stores_csv_path, orders_dw_engine)
    logger.info("Stores loaded successfully")

    products_json_path: Path = get_customer_orders_products_json_path()

    logger.info("Starting products ingestion")
    ingest_products(products_json_path, orders_dw_engine)
    logger.info("Products loaded successfully")

    order_rows_parquet_file_path = get_order_rows_parquet_path()

    logger.info("Starting order rows ingestion")
    ingest_order_rows(order_rows_parquet_file_path, customer_orders_engine, orders_dw_engine)
    logger.info("Order rows loaded successfully")

    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
