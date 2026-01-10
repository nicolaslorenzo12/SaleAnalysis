from __future__ import annotations

from typing import Optional

from models.customer_orders.raw.raw_customer import RawCustomer
from models.customer_orders.transformed.transformed_customer import TransformedCustomer


def _build_full_name(
    given: Optional[str],
    surname: Optional[str],
) -> Optional[str]:
    parts = [
        given,
        surname,
    ]
    parts = [p for p in parts if p]
    return " ".join(parts) if parts else None



def transform_customers(raw_customers: list[RawCustomer]) -> list[TransformedCustomer]:
    return [
        TransformedCustomer(
            CustomerKey=raw_customer.CustomerKey,
            Gender=raw_customer.Gender,
            FullName=_build_full_name(raw_customer.GivenName, raw_customer.Surname),
            City=raw_customer.City,
            State=raw_customer.StateFull,
            StateCode=raw_customer.State,
            Country=raw_customer.CountryFull,
            CountryCode=raw_customer.Country,
            Birthday=raw_customer.Birthday,
        )
        for raw_customer in raw_customers
    ]

