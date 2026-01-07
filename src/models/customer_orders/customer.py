from datetime import date
from typing import Optional, get_origin, get_args

from pydantic import BaseModel, Field, field_validator


class Customer(BaseModel):
    CustomerKey: int
    GeoAreaKey: Optional[int] = None

    StartDT: Optional[date] = None
    EndDT: Optional[date] = None

    Continent: Optional[str] = None
    Gender: Optional[str] = None
    Title: Optional[str] = None
    GivenName: Optional[str] = None
    MiddleInitial: Optional[str] = None
    Surname: Optional[str] = None
    StreetAddress: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    StateFull: Optional[str] = None
    ZipCode: Optional[str] = None
    Country: Optional[str] = None
    CountryFull: Optional[str] = None

    Birthday: Optional[date] = None
    Age: Optional[int] = None
    Occupation: Optional[str] = None
    Company: Optional[str] = None
    Vehicle: Optional[str] = None

    Latitude: Optional[float] = None
    Longitude: Optional[float] = None



    model_config = {
        "from_attributes": True,
    }
