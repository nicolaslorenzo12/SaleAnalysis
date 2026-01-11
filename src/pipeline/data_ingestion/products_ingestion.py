import logging
from pathlib import Path

from sqlalchemy import Engine

from models.customer_orders.raw.raw_store import RawStore
from models.customer_orders.transformed.transformed_product import TransformedProduct
from pipeline.data_ingestion.extractors.raw_products_extractor import extract_raw_products_from_json
from pipeline.data_ingestion.loaders.products_loader import load_products
from pipeline.data_ingestion.transformers.products_transformer import transform_products

logger = logging.getLogger(__name__)


def ingest_products(products_json_file_path: Path,  orders_dw_engine: Engine):
    logger.info("Extracting products")
    raw_product_list: list[RawStore] = extract_raw_products_from_json(products_json_file_path)
    logger.info("Transforming products")
    transformed_product_list: list[TransformedProduct] = transform_products(raw_product_list)
    logger.info("Loading products")
    load_products(orders_dw_engine, transformed_product_list)