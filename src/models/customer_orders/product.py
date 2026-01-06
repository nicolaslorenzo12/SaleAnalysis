from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    ProductKey: int = Field(..., ge=1)
    ProductCode: str = Field(..., max_length=50)
    ProductName: str = Field(..., max_length=200)

    Manufacturer: str = Field(..., max_length=100)
    Brand: str = Field(..., max_length=100)
    Color: Optional[str] = Field(None, max_length=50)

    WeightUnit: Optional[str] = Field(None, max_length=50)
    Weight: Optional[float] = Field(None, ge=0)

    Cost: float = Field(..., ge=0)
    Price: float = Field(..., ge=0)

    CategoryKey: int = Field(..., ge=1)
    CategoryName: str = Field(..., max_length=100)

    SubCategoryKey: int = Field(..., ge=1)
    SubCategoryName: str = Field(..., max_length=100)

    model_config = {
        "from_attributes": True,
        "extra": "forbid",
        "validate_assignment": True,
    }
