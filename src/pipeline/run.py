from pathlib import Path

from dotenv import load_dotenv
load_dotenv()
import os

STORES_PATH = Path(os.environ["CUSTOMER_ORDERS_STORES_CSV_PATH"])

from sqlalchemy import Engine
from extractors.customer_orders.sources.customer_orders_db_engine import get_engine
from extractors.customer_orders.sources.customer_orders_db_repository import get_customers, get_orders, get_currency_exchanges
from extractors.customer_orders.sources.stores_csv_repository import get_stores_from_csv


def main() -> None:
    engine:Engine = get_engine()
    customer_list = get_customers(engine)
    order_list = get_orders(engine)
    currency_exchange_list = get_currency_exchanges(engine)
    store_list = get_stores_from_csv(STORES_PATH)

    for customer in customer_list[:5]:
        print(customer)

    for order in order_list[:5]:
        print(order)

    for currency_exchange in currency_exchange_list[:5]:
        print(currency_exchange)

    for store in store_list[:5]:
        print(store)


if __name__ == "__main__":
    main()
