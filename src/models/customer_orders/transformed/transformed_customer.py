from datetime import date
from typing import Optional, get_origin, get_args

from pydantic import BaseModel, Field, field_validator


class TransformedCustomer(BaseModel):
    CustomerKey: int
    Gender: Optional[str] = None
    FullName: Optional[str] = None
    City: Optional[str] = None
    StateCode: Optional[str] = None
    StateName: Optional[str] = None
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None
    Birthday: Optional[date] = None
