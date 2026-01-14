from dataclasses import dataclass
from typing import Optional


@dataclass
class TransformedProduct:
    ProductKey: int
    ProductName: Optional[str] = None
    Brand: Optional[str] = None
    Color: Optional[str] = None
    CategoryKey: Optional[int] = None
    CategoryName: Optional[str] = None
    SubCategoryKey: Optional[int] = None
    SubCategoryName: Optional[str] = None