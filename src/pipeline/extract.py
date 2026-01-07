from pathlib import Path
from dotenv import load_dotenv

from models.extracted_data.customer_orders_extracted_data import CustomerOrdersExtractedData

load_dotenv()
from sqlalchemy import Engine
from pipeline.loaders.customer_orders.sources.db_tables_loader import load_customers, load_orders, \
    load_currency_exchanges
from pipeline.loaders.customer_orders.sources.order_rows_loader import load_order_rows_from_parquet
from pipeline.loaders.customer_orders.sources.products_loader import load_products_from_json
from pipeline.loaders.customer_orders.sources.stores_loader import load_stores_from_csv


def extract_data(engine: Engine, stores_path:Path, products_path: Path, order_rows_path: Path) -> CustomerOrdersExtractedData:
    customer_list = load_customers(engine)
    order_list = load_orders(engine)
    currency_exchange_list = load_currency_exchanges(engine)
    store_list = load_stores_from_csv(stores_path)
    products_list = load_products_from_json(products_path)
    order_rows_list = load_order_rows_from_parquet(order_rows_path)

    customer_orders_all_extracted_data = CustomerOrdersExtractedData(customer_list, order_list, currency_exchange_list,
                                                                     store_list, products_list, order_rows_list)

    return customer_orders_all_extracted_data