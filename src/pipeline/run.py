from __future__ import annotations

import logging
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import Engine

from pipeline.config.file_paths.store_csv_file_path import get_customer_orders_stores_csv_path
from pipeline.data_ingestion.date_ingestion import ingest_dates
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

    logger.info("Starting date data ingestion")
    ingest_dates(customer_orders_engine, orders_dw_engine)
    logger.info("Dates loaded successfully")

    stores_csv_path: Path = get_customer_orders_stores_csv_path()

    logger.info("Starting store data ingestion")
    ingest_stores(stores_csv_path, orders_dw_engine)
    logger.info("Stores loaded successfully")

if __name__ == "__main__":
    run_pipeline()
