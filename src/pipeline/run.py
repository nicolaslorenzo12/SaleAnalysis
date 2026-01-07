from pathlib import Path

from dotenv import load_dotenv

from pipeline.loaders.customer_orders.sources.db_tables_loader import load_customers, load_orders, \
    load_currency_exchanges
from pipeline.loaders.customer_orders.sources.order_rows_loader import load_order_rows_from_parquet
from pipeline.loaders.customer_orders.sources.products_loader import load_products_from_json

load_dotenv()
import os

STORES_PATH = Path(os.environ["CUSTOMER_ORDERS_STORES_CSV_PATH"])
PRODUCTS_PATH = Path(os.environ["PRODUCTS_JSON_PATH"])
ORDER_ROWS_PATH = Path(os.environ["ORDER_ROWS_PARQUET_PATH"])

from sqlalchemy import Engine
from pipeline.loaders.customer_orders.sources.customer_orders_db_engine import get_engine
from pipeline.loaders.customer_orders.sources.stores_loader import load_stores_from_csv


def main() -> None:
    engine:Engine = get_engine()
    customer_list = load_customers(engine)
    order_list = load_orders(engine)
    currency_exchange_list = load_currency_exchanges(engine)
    store_list = load_stores_from_csv(STORES_PATH)
    products_list = load_products_from_json(PRODUCTS_PATH)
    order_rows_list = load_order_rows_from_parquet(ORDER_ROWS_PATH)

    for customer in customer_list[:5]:
        print(customer)

    for order in order_list[:5]:
        print(order)

    for currency_exchange in currency_exchange_list[:5]:
        print(currency_exchange)

    for store in store_list[:5]:
        print(store)

    for product in products_list[:5]:
        print(product)

    for order_row in order_rows_list[:5]:
        print(order_row)


if __name__ == "__main__":
    main()
