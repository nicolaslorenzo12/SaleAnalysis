import logging
from sqlalchemy import Engine

logger = logging.getLogger(__name__)

from models.orders_DW.transformed.transformed_customer import TransformedCustomer
from models.customer_orders.raw.raw_customer import RawCustomer
from pipeline.data_ingestion.extractors.raw_customers_extractor import extract_raw_customers
from pipeline.data_ingestion.transformers.customers_transformer import transform_customers
from pipeline.data_ingestion.loaders.customers_loader import load_customers


def ingest_customers(customer_orders_engine: Engine, orders_dw_engine: Engine):
    logger.info("Extracting customers")
    raw_customer_list: list[RawCustomer] = extract_raw_customers(customer_orders_engine)
    logger.info("Transforming customers")
    transformed_customer_list: list[TransformedCustomer] = transform_customers(raw_customer_list)
    logger.info("Loading customers")
    load_customers(orders_dw_engine, transformed_customer_list)