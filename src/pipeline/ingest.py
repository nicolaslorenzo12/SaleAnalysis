from pathlib import Path

from models.extracted_data.customer_orders_extracted_data import CustomerOrdersExtractedData
from sqlalchemy import Engine

from pipeline.extractors.customer_orders.raw_currency_exchanges_extractor import extract_raw_currency_exchanges
from pipeline.extractors.customer_orders.raw_customers_extractor import extract_raw_customers
from pipeline.extractors.customer_orders.raw_order_rows_extractor import extract_raw_order_rows_from_parquet
from pipeline.extractors.customer_orders.raw_orders_extractor import extract_raw_orders
from pipeline.extractors.customer_orders.raw_products_extractor import extract_raw_products_from_json
from pipeline.extractors.customer_orders.raw_stores_extractor import extract_raw_stores_from_csv


def ingest_data(engine: Engine, stores_path:Path, products_path: Path, order_rows_path: Path) -> CustomerOrdersExtractedData:
    customer_list = extract_raw_customers(engine)
    order_list = extract_raw_orders(engine)
    currency_exchange_list = extract_raw_currency_exchanges(engine)
    store_list = extract_raw_stores_from_csv(stores_path)
    products_list = extract_raw_products_from_json(products_path)
    order_rows_list = extract_raw_order_rows_from_parquet(order_rows_path)

    customer_orders_all_extracted_data = CustomerOrdersExtractedData(customer_list, order_list, currency_exchange_list,
                                                                     store_list, products_list, order_rows_list)

    return customer_orders_all_extracted_data