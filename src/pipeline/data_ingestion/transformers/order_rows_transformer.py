from __future__ import annotations

from typing import Optional

from models.customer_orders.raw.raw_customer import RawCustomer
from models.orders_DW.staged.staged_order_row import StagedOrderRow
from models.orders_DW.transformed.tranformed_order_row import TransformedOrderRow
from models.orders_DW.transformed.transformed_customer import TransformedCustomer



def transform_order_rows(staged_order_rows: list[StagedOrderRow]) -> list[TransformedOrderRow]:
    return [
        TransformedOrderRow(
            OrderKey=staged_order_row.OrderKey,
            LineNumber=staged_order_row.LineNumber,
            ProductKey=staged_order_row.ProductKey,
            CustomerKey=staged_order_row.CustomerKey,
            StoreKey=staged_order_row.StoreKey,
            Quantity=staged_order_row.Quantity,
            OrderDate=staged_order_row.OrderDate,
            UnitPriceInUSD=staged_order_row.UnitPrice * staged_order_row.ExchangeToUsd,
            NetPriceInUSD=staged_order_row.NetPrice * staged_order_row.ExchangeToUsd,
            UnitCostInUSD=staged_order_row.UnitCost * staged_order_row.ExchangeToUsd,
        )
        for staged_order_row in staged_order_rows
    ]