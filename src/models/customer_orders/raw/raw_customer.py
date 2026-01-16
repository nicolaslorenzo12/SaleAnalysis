from datetime import date
from typing import Optional

from pydantic import BaseModel


class RawCustomer(BaseModel):
    CustomerKey: int
    GeoAreaKey: int

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

    Birthday: date
    Age: int
    Occupation: str
    Company: Optional[str] = None
    Vehicle: Optional[str] = None

    Latitude: float
    Longitude: float



    model_config = {
        "from_attributes": True,
    }
