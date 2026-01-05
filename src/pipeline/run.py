from sqlalchemy import Engine
from db.customer_orders.connection import get_engine
from db.customer_orders.tables import get_customers


def main() -> None:
    engine:Engine = get_engine()
    customer_list = get_customers(engine)

    # Print first few customers
    for customer in customer_list[:5]:
        print(customer)


if __name__ == "__main__":
    main()
