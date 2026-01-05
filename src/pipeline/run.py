from sqlalchemy import Engine
from customer_orders.sources.db_engine import get_engine
from customer_orders.sources.db_repository import get_customers, get_orders, get_currency_exchanges


def main() -> None:
    engine:Engine = get_engine()
    customer_list = get_customers(engine)
    order_list = get_orders(engine)
    currency_exchange_list = get_currency_exchanges(engine)

    for customer in customer_list[:5]:
        print(customer)

    for order in order_list[:5]:
        print(order)

    for currency_exchange in currency_exchange_list[:5]:
        print(currency_exchange)


if __name__ == "__main__":
    main()
