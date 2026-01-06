from __future__ import annotations

import pandas as pd
from sqlalchemy import Engine

from models.customer_orders.customer import Customer
from models.customer_orders.order import Order
from models.customer_orders.currency_exchange import CurrencyExchange


def load_customers(engine: Engine) -> list[Customer]:
    df_customers = pd.read_sql("SELECT * FROM [dbo].[Customer]", engine)
    return [Customer.model_validate(customer) for customer in df_customers.to_dict(orient="records")]


def load_orders(engine: Engine) -> list[Order]:
    df_orders = pd.read_sql("SELECT * FROM [dbo].[Orders]", engine)
    return [Order.model_validate(order) for order in df_orders.to_dict(orient="records")]


def load_currency_exchanges(engine: Engine) -> list[CurrencyExchange]:
    df_currency_exchange = pd.read_sql("SELECT * FROM [dbo].[CurrencyExchange]", engine)
    return [CurrencyExchange.model_validate(currency_exchange) for currency_exchange in df_currency_exchange.to_dict(orient="records")]
