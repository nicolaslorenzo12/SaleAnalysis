import logging
from sqlalchemy import Engine

from models.customer_orders.raw.raw_date import RawDate
from pipeline.data_ingestion.extractors.raw_dates_extractor import extract_raw_dates
from pipeline.data_ingestion.loaders.dates_loader import load_dates
from pipeline.data_ingestion.transformers.dates_transformer import transform_dates

logger = logging.getLogger(__name__)

from models.orders_DW.transformed.transformed_customer import TransformedCustomer


def ingest_dates(customer_orders_engine: Engine, orders_dw_engine: Engine):
    logger.info("Extracting dates")
    raw_date_list: list[RawDate] = extract_raw_dates(customer_orders_engine)
    logger.info("Transforming dates")
    transformed_date_list: list[TransformedCustomer] = transform_dates(raw_date_list)
    logger.info("Loading dates")
    load_dates(orders_dw_engine, transformed_date_list)