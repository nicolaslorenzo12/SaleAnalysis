from typing import Optional
from pydantic import BaseModel, Field, field_validator


class RawProduct(BaseModel):
    ProductKey: int
    ProductCode: str
    ProductName: Optional[str] = None

    Manufacturer: Optional[str] = None
    Brand: Optional[str] = None
    Color: Optional[str] = None

    WeightUnit: Optional[str] = None
    Weight: Optional[float] = None

    Cost: Optional[float] = None
    Price: Optional[float] = None

    CategoryKey: Optional[int] = None
    CategoryName: Optional[str] = None

    SubCategoryKey: Optional[int] = None
    SubCategoryName: Optional[str] = None