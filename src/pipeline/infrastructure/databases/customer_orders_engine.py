from dotenv import load_dotenv
load_dotenv()
import os
from functools import lru_cache
from urllib.parse import quote_plus

import sqlalchemy
from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError

from models.errors.db import DatabaseConnectionError
from models.errors.enviroment_variables import MissingEnvironmentVariableError
from models.db_connection.sql_config import SqlConfig


def raise_if_missing_env_vars(missing: list[str]) -> None:
    if missing:
        raise MissingEnvironmentVariableError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

def load_sql_config() -> SqlConfig:
    required_env_vars = {
        "SQL_USER": os.getenv("SQL_USER"),
        "SQL_PASSWORD": os.getenv("SQL_PASSWORD"),
        "SQL_SERVER": os.getenv("SQL_SERVER"),
        "SQL_DATABASE_CUSTOMER_ORDERS": os.getenv("SQL_DATABASE_CUSTOMER_ORDERS"),
    }

    missing = [k for k, v in required_env_vars.items() if not v]
    raise_if_missing_env_vars(missing)

    return SqlConfig(
        user=required_env_vars["SQL_USER"],
        password=required_env_vars["SQL_PASSWORD"],
        server=required_env_vars["SQL_SERVER"],
        database=required_env_vars["SQL_DATABASE_CUSTOMER_ORDERS"],
    )


def build_connection_string(cfg: SqlConfig) -> str:

    pw = quote_plus(cfg.password)
    return (
        f"mssql+pyodbc://{cfg.user}:{pw}@{cfg.server}/{cfg.database}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )


@lru_cache(maxsize=1)
def get_engine() -> Engine:
    cfg = load_sql_config()
    connection_string = build_connection_string(cfg)

    try:
        engine = sqlalchemy.create_engine(connection_string, future=True)

        with engine.connect():
            pass

        return engine

    except SQLAlchemyError as exc:
        raise DatabaseConnectionError(
            "Failed to connect to the SQL Server database"
        ) from exc