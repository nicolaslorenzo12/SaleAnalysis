from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Customer(BaseModel):
    CustomerKey: int = Field(..., ge=1)
    GeoAreaKey: int = Field(..., ge=1)

    StartDT: Optional[date] = None
    EndDT: Optional[date] = None

    Continent: Optional[str] = Field(None, max_length=50)
    Gender: Optional[str] = Field(None, max_length=10)
    Title: Optional[str] = Field(None, max_length=50)
    GivenName: Optional[str] = Field(None, max_length=150)
    MiddleInitial: Optional[str] = Field(None, max_length=150)
    Surname: Optional[str] = Field(None, max_length=150)
    StreetAddress: Optional[str] = Field(None, max_length=150)
    City: Optional[str] = Field(None, max_length=50)
    State: Optional[str] = Field(None, max_length=50)
    StateFull: Optional[str] = Field(None, max_length=50)
    ZipCode: Optional[str] = Field(None, max_length=50)
    Country: Optional[str] = Field(None, max_length=50)
    CountryFull: Optional[str] = Field(None, max_length=50)

    Birthday: date
    Age: int = Field(..., ge=0, le=150)

    Occupation: Optional[str] = Field(None, max_length=100)
    Company: Optional[str] = Field(None, max_length=50)
    Vehicle: Optional[str] = Field(None, max_length=50)

    Latitude: float = Field(..., ge=-90, le=90)
    Longitude: float = Field(..., ge=-180, le=180)


    model_config = {
        "from_attributes": True,
        "extra": "forbid",
        "validate_assignment": True,
    }
