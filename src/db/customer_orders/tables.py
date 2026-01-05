import pandas as pd
from sqlalchemy import Engine

from models.customer_orders.currency_exchange import CurrencyExchange
from models.customer_orders.customer import Customer
from models.customer_orders.order import Order


def get_customers(engine: Engine) -> list[Customer]:
    customers: list[Customer] = pd.read_sql(
        "SELECT * FROM [dbo].[Customer]",
        engine
    ).to_dict(orient="records")

    return [Customer.model_validate(customer) for customer in customers]

def get_orders(engine: Engine) -> list[Order]:
    orders: list[Order] =  pd.read_sql(
        "SELECT * FROM [dbo].[Orders]",
        engine
    ).to_dict(orient="records")

    return [Order.model_validate(order) for order in orders]

def get_currency_exchanges(engine: Engine) -> list[CurrencyExchange]:
    currency_exchanges: list[CurrencyExchange] =  pd.read_sql(
        "SELECT * FROM [dbo].[CurrencyExchange]",
        engine
    ).to_dict(orient="records")

    return [CurrencyExchange.model_validate(currency_exchange) for currency_exchange in currency_exchanges]



