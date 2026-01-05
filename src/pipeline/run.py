from sqlalchemy import Engine
from db.customer_orders.connection import get_engine
from db.customer_orders.tables import get_customers, get_orders, get_currency_exchanges


def main() -> None:
    engine:Engine = get_engine()
    customer_list = get_customers(engine)
    order_list = get_orders(engine)
    currency_exchange_list = get_currency_exchanges(engine)

    for currency_exchange in currency_exchange_list[:5]:
        print(currency_exchange)


if __name__ == "__main__":
    main()
