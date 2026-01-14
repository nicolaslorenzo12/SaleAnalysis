from decimal import Decimal
from typing import List

from models.customer_orders.raw.raw_currency_exchange import RawCurrencyExchange
from models.customer_orders.raw.raw_order import RawOrder
from models.customer_orders.raw.raw_order_row import RawOrderRow
from models.orders_DW.staged.staged_order_row import StagedOrderRow

# Base currency
BASE_CCY = "USD"


# Build foreign exchange to use
def _build_fx_to_usd_lookup(
    currency_exchanges: List[RawCurrencyExchange],
) -> dict[tuple, Decimal]:
    return {
        (fx.Date, fx.FromCurrency): Decimal(str(fx.Exchange))
        for fx in currency_exchanges
        if fx.ToCurrency == BASE_CCY
    }


def _build_staged_order_row(
    row: RawOrderRow,
    order: RawOrder,
    fx_to_usd: dict[tuple, Decimal],
) -> StagedOrderRow:
    return StagedOrderRow(
        OrderKey=row.OrderKey,
        LineNumber=row.LineNumber,
        ProductKey=row.ProductKey,
        CustomerKey=order.CustomerKey,
        StoreKey=order.StoreKey,
        Quantity=row.Quantity,
        UnitPrice=row.UnitPrice,
        NetPrice=row.NetPrice,
        UnitCost=row.UnitCost,
        OrderDate=order.OrderDate,
        CurrencyCode=order.CurrencyCode,
        ExchangeToUsd=fx_to_usd[(order.OrderDate, order.CurrencyCode)],
    )


def stage_order_rows(
    order_rows: List[RawOrderRow],
    orders: List[RawOrder],
    currency_exchanges: List[RawCurrencyExchange],
) -> List[StagedOrderRow]:

    orders_by_key = {o.OrderKey: o for o in orders}
    fx_to_usd = _build_fx_to_usd_lookup(currency_exchanges)

    staged_rows: List[StagedOrderRow] = []
    for order_row in order_rows:
        order = orders_by_key[order_row.OrderKey]
        staged_rows.append(_build_staged_order_row(order_row, order, fx_to_usd))

    return staged_rows
