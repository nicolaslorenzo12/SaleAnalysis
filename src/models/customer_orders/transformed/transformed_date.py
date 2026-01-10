from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class TransformedDate:
    DateKey: int
    Date: date
    Year: int
    Quarter: str
    Month: str
    MonthNumber: int
    DayofWeek: str
    DayofWeekNumber: int
    IsItAWorkingDay: bool
