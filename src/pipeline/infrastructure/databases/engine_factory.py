from __future__ import annotations
import logging
import os
from functools import lru_cache
from urllib.parse import quote_plus

import sqlalchemy
from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError

from models.db_connection.sql_config import SqlConfig
from models.errors.db import DatabaseConnectionError
from models.errors.enviroment_variables import MissingEnvironmentVariableError

logger = logging.getLogger(__name__)

class SqlEngineFactory:

    @staticmethod
    def _raise_if_missing_env_vars(env_variables: list[str]) -> None:
        if env_variables:
            raise MissingEnvironmentVariableError(
                f"Missing required environment variables: {', '.join(env_variables)}"
            )

    @staticmethod
    def _load_sql_config(database_env_var: str) -> SqlConfig:
        required_env_vars = {
            "SQL_USER": os.getenv("SQL_USER"),
            "SQL_PASSWORD": os.getenv("SQL_PASSWORD"),
            "SQL_SERVER": os.getenv("SQL_SERVER"),
            database_env_var: os.getenv(database_env_var),
        }

        env_variables = [k for k, v in required_env_vars.items() if not v]
        SqlEngineFactory._raise_if_missing_env_vars(env_variables)

        return SqlConfig(
            user=required_env_vars["SQL_USER"],
            password=required_env_vars["SQL_PASSWORD"],
            server=required_env_vars["SQL_SERVER"],
            database=required_env_vars[database_env_var],
        )

    @staticmethod
    def _build_connection_string(cfg: SqlConfig) -> str:
        pw = quote_plus(cfg.password)
        return (
            f"mssql+pyodbc://{cfg.user}:{pw}@{cfg.server}/{cfg.database}"
            "?driver=ODBC+Driver+17+for+SQL+Server"
        )

    @staticmethod
    def _create_engine(database_env_var: str) -> Engine:
        cfg = SqlEngineFactory._load_sql_config(database_env_var)
        connection_string = SqlEngineFactory._build_connection_string(cfg)

        try:
            engine = sqlalchemy.create_engine(
                connection_string,
                future=True,
                pool_pre_ping=True,
            )

            with engine.connect():

                logger.info(
                    "Successfully connected to SQL Server database '%s' using env var '%s'",
                    cfg.database,
                    database_env_var,
                )

            return engine

        except SQLAlchemyError as exc:
            raise DatabaseConnectionError(
                f"Failed to connect to the SQL Server database (env: {database_env_var})"
            ) from exc

    @staticmethod
    @lru_cache(maxsize=None)
    def get_engine(database_env_var: str) -> Engine:
        return SqlEngineFactory._create_engine(database_env_var)
