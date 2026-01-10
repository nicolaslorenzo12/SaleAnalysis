from __future__ import annotations

from models.customer_orders.raw.raw_date import RawDate
from models.customer_orders.transformed.transformed_date import TransformedDate

def transform_dates(raw_dates: list[RawDate]) -> list[TransformedDate]:
    return [
        TransformedDate(
            DateKey=raw_date.DateKey,
            Date=raw_date.Date,
            Year=raw_date.Year,
            Quarter=raw_date.Quarter,
            Month=raw_date.Month,
            MonthNumber=raw_date.MonthNumber,
            DayofWeek=raw_date.DayofWeek,
            DayofWeekNumber=raw_date.DayofWeekNumber,
            IsItAWorkingDay=bool(raw_date.WorkingDay)
        )
        for raw_date in raw_dates
    ]
