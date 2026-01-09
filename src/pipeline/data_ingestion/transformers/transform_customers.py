from __future__ import annotations

from typing import List, Optional

from models.customer_orders.raw.raw_customer import RawCustomer
from models.customer_orders.transformed.transformed_customer import TransformedCustomer
from pipeline.utils.strings import strip_string


def _build_full_name(
    given: Optional[str],
    surname: Optional[str],
) -> Optional[str]:
    parts = [
        strip_string(given),
        strip_string(surname),
    ]
    parts = [p for p in parts if p]
    return " ".join(parts) if parts else None



def transform_customers(raw_customers: list[RawCustomer]) -> list[TransformedCustomer]:
    return [
        TransformedCustomer(
            CustomerKey=raw_customer.CustomerKey,
            Gender=strip_string(raw_customer.Gender),
            FullName=_build_full_name(raw_customer.GivenName, raw_customer.Surname),
            City=strip_string(raw_customer.City),
            State=strip_string(raw_customer.StateFull),
            Country=strip_string(raw_customer.CountryFull),
            Birthday=raw_customer.Birthday,
        )
        for raw_customer in raw_customers
    ]

