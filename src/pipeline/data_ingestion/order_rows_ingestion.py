import logging
from pathlib import Path

from sqlalchemy import Engine

from models.customer_orders.raw.raw_currency_exchange import RawCurrencyExchange
from models.customer_orders.raw.raw_order import RawOrder
from models.customer_orders.raw.raw_order_row import RawOrderRow
from pipeline.data_ingestion.extractors.raw_currency_exchanges_extractor import extract_raw_currency_exchanges
from pipeline.data_ingestion.extractors.raw_order_rows_extractor import extract_raw_order_rows_from_parquet
from pipeline.data_ingestion.extractors.raw_orders_extractor import extract_raw_orders
from pipeline.data_ingestion.loaders.order_rows_loader import load_order_rows
from pipeline.data_ingestion.transformers.order_rows_transformer import transform_order_rows

logger = logging.getLogger(__name__)


def ingest_order_rows(order_rows_parquet_path: Path, customer_orders_engine: Engine,  orders_dw_engine: Engine):
    logger.info("Extracting order rows")
    raw_order_row_list: list[RawOrderRow] = extract_raw_order_rows_from_parquet(order_rows_parquet_path)
    logger.info("Extracting orders")
    raw_order_list: list[RawOrder] = extract_raw_orders(customer_orders_engine)
    logger.info("Extracting currency exchange rates")
    raw_currency_exchange_list: list[RawCurrencyExchange] = extract_raw_currency_exchanges(customer_orders_engine)
    logger.info("Transforming order rows")
    transformed_order_row_list = transform_order_rows(raw_order_row_list, raw_order_list, raw_currency_exchange_list)
    logger.info("Loading order rows")
    load_order_rows(orders_dw_engine, transformed_order_row_list)