from __future__ import annotations

from typing import List, Optional

from models.customer_orders.raw.raw_customer import RawCustomer
from models.customer_orders.normalized.normalized_customer import NormalizedCustomer
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



def normalize_customers(raw_customers: List[RawCustomer]) -> List[NormalizedCustomer]:

    normalized_customers: List[NormalizedCustomer] = []

    for raw_customer in raw_customers:
        normalized_customers.append(
            NormalizedCustomer(
                CustomerKey=raw_customer.CustomerKey,
                Gender=strip_string(raw_customer.Gender),
                FullName=_build_full_name(raw_customer.GivenName, raw_customer.Surname),
                City=strip_string(raw_customer.City),
                StateCode=strip_string(raw_customer.State),
                StateName=strip_string(raw_customer.StateFull),
                CountryCode=strip_string(raw_customer.Country),
                CountryName=strip_string(raw_customer.CountryFull),
                Birthday=raw_customer.Birthday,
            )
        )

    return normalized_customers
