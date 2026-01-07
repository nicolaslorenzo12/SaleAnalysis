import math
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator, computed_field


class Store(BaseModel):
    StoreKey: int
    StoreCode: int
    GeoAreaKey: Optional[int] = None

    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None
    State: Optional[str] = None

    OpenDate: Optional[date] = None
    CloseDate: Optional[date] = None

    Description: Optional[str] = None
    SquareMeters: Optional[int] = None
    Status: Optional[str] = None

    @field_validator(
        "CountryCode", "CountryName", "State", "Description", "Status",
        "OpenDate", "CloseDate", "SquareMeters",
        mode="before",
    )
    @classmethod
    def normalize_csv_missing(cls, v):
        # pandas NaN
        if isinstance(v, float) and math.isnan(v):
            return None
        # empty strings from CSV
        if v == "":
            return None
        return v

