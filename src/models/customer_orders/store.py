import math
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator, computed_field


class Store(BaseModel):
    StoreKey: int = Field(..., ge=1)

    # -1 = not applicable (e.g., Online store), >=1 = physical store values
    StoreCode: int = Field(..., ge=-1)
    GeoAreaKey: int = Field(..., ge=-1)

    CountryCode: Optional[str] = Field(None, max_length=50)
    CountryName: Optional[str] = Field(None, max_length=50)
    State: Optional[str] = Field(None, max_length=100)

    OpenDate: Optional[date] = None
    CloseDate: Optional[date] = None

    Description: Optional[str] = Field(None, max_length=100)
    SquareMeters: Optional[int] = Field(None, ge=0)
    Status: Optional[str] = Field(None, max_length=50)

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


    model_config = {
        "extra": "forbid",
        "validate_assignment": True,
    }
