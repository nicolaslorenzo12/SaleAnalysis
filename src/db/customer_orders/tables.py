import pandas as pd
from sqlalchemy import Engine

from models.customer_orders.customer import Customer


def get_customers(engine: Engine) -> list[Customer]:
    rows = pd.read_sql(
        "SELECT * FROM [dbo].[Customer]",
        engine
    ).to_dict(orient="records")

    return [Customer.model_validate(row) for row in rows]

def orders(engine: Engine) -> pd.DataFrame:
    return pd.read_sql(
        "SELECT * FROM [dbo].[Orders]",
        engine
    )

def currency_exchange(engine: Engine) -> pd.DataFrame:
    return pd.read_sql(
        "SELECT * FROM [dbo].[CurrencyExchange]",
        engine
    )
