from __future__ import annotations

import sqlalchemy
from sqlalchemy import Engine, text

from models.customer_orders.customer import Customer
from models.customer_orders.order import Order
from models.customer_orders.currency_exchange import CurrencyExchange


def load_customers(engine: Engine) -> list[Customer]:
    with engine.connect() as conn:
        customers: list[sqlalchemy.engine.RowMapping] = conn.execute(text("SELECT * FROM [dbo].[Customer]")).mappings().all()
    return [Customer.model_validate(dict(customer)) for customer in customers]


def load_orders(engine: Engine) -> list[Order]:
    with engine.connect() as conn:
        orders: list[sqlalchemy.engine.RowMapping] = conn.execute(text("SELECT * FROM [dbo].[Orders]")).mappings().all()
    return [Order.model_validate(dict(order)) for order in orders]


def load_currency_exchanges(engine: Engine) -> list[CurrencyExchange]:
    with engine.connect() as conn:
        currency_exchanges: list[sqlalchemy.engine.RowMapping] = conn.execute(text("SELECT * FROM [dbo].[CurrencyExchange]")).mappings().all()
    return [CurrencyExchange.model_validate(dict(currency_exchange)) for currency_exchange in currency_exchanges]
