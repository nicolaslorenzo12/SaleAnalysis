import logging
from pathlib import Path

from sqlalchemy import Engine

from models.customer_orders.raw.raw_store import RawStore
from models.orders_DW.transformed.transformed_store import TransformedStore
from pipeline.data_ingestion.extractors.raw_stores_extractor import extract_raw_stores_from_csv
from pipeline.data_ingestion.loaders.stores_loader import load_stores
from pipeline.data_ingestion.transformers.stores_transformer import transform_stores

logger = logging.getLogger(__name__)


def ingest_stores(store_csv_file_path: Path,  orders_dw_engine: Engine):
    logger.info("Extracting stores")
    raw_store_list: list[RawStore] = extract_raw_stores_from_csv(store_csv_file_path)
    logger.info("Transforming stores")
    transformed_store_list: list[TransformedStore] = transform_stores(raw_store_list)
    logger.info("Loading stores")
    load_stores(orders_dw_engine, transformed_store_list)