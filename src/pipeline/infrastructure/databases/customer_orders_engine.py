from sqlalchemy import Engine
from pipeline.infrastructure.databases.engine_factory import SqlEngineFactory


def get_customer_orders_engine() -> Engine:
    return SqlEngineFactory.get_engine("SQL_DATABASE_CUSTOMER_ORDERS")
