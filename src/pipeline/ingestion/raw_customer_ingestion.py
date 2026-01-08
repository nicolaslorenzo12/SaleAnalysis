from sqlalchemy import Engine

from models.customer_orders.normalized.normalized_customer import NormalizedCustomer
from models.customer_orders.raw.raw_customer import RawCustomer
from pipeline.ingestion.extractors.raw_customers_extractor import extract_raw_customers
from pipeline.ingestion.normalization.normalize_customers import normalize_customers
from pipeline.ingestion.stage_loaders.customers_stage_loader import load_stg_customers


def ingest_customers(customer_orders_engine: Engine, orders_dw_engine: Engine):
    raw_customer_list: list[RawCustomer] = extract_raw_customers(customer_orders_engine)
    normalized_customer_list: list[NormalizedCustomer] = normalize_customers(raw_customer_list)
    load_stg_customers(orders_dw_engine, normalized_customer_list)