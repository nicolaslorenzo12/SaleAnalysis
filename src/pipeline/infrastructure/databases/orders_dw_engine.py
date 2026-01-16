from sqlalchemy import Engine

from pipeline.infrastructure.databases.engine_factory import SqlEngineFactory


def get_orders_dw_engine() -> Engine:
    return SqlEngineFactory.get_engine("SQL_DATABASE_ORDERS_DW")
