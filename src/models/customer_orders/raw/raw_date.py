from datetime import date
from pydantic import BaseModel


class RawDate(BaseModel):
    Date: date
    DateKey: int
    Year: int
    YearQuarter: str
    YearQuarterNumber: int
    Quarter: str
    YearMonth: str
    YearMonthShort: str
    YearMonthNumber: int
    Month: str
    MonthShort: str
    MonthNumber: int
    DayofWeek: str
    DayofWeekShort: str
    DayofWeekNumber: int
    WorkingDay: int
    WorkingDayNumber: int
