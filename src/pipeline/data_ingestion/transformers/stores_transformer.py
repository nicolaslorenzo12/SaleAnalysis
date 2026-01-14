from __future__ import annotations
from models.customer_orders.raw.raw_store import RawStore
from models.orders_DW.transformed.transformed_store import TransformedStore


def _normalize_country_code(value: str | None) -> str | None:
    return None if value == "--" else value


def transform_stores(raw_stores: list[RawStore]) -> list[TransformedStore]:
    return [
        TransformedStore(
            StoreKey=raw_store.StoreKey,
            State=raw_store.State,
            Country=raw_store.CountryName,
            CountryCode=_normalize_country_code(raw_store.CountryCode),
        )
        for raw_store in raw_stores
    ]