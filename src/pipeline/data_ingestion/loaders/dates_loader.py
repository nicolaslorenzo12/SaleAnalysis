from __future__ import annotations
from sqlalchemy import Engine, text
from models.customer_orders.transformed.transformed_date import TransformedDate
from pipeline.data_ingestion.loaders.shared.rows_loader import load_table
DM_DATE_TABLE = "dbo.dm_date"

def load_dates(
    dw_engine: Engine,
    dates_to_load: list[TransformedDate],
    *,
    truncate: bool = True,
    batch_size: int = 5000,
) -> None:
    insert_sql = text(f"""
        INSERT INTO {DM_DATE_TABLE}
        (
            DateKey, Date, Year, Quarter, Month,
            MonthNumber, DayofWeek, DayofWeekNumber,
            IsItAWorkingDay
        )
        VALUES
        (
            :DateKey, :Date, :Year, :Quarter,
            :Month, :MonthNumber ,:DayofWeek, :DayofWeekNumber,
             :IsItAWorkingDay
        )
    """)

    load_table(
        engine=dw_engine,
        table_name=DM_DATE_TABLE,
        insert_sql=insert_sql,
        items=dates_to_load,
        truncate=truncate,
        batch_size=batch_size,
    )