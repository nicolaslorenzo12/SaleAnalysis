from dataclasses import dataclass

from models.customer_orders.currency_exchange import CurrencyExchange
from models.customer_orders.customer import Customer
from models.customer_orders.order import Order
from models.customer_orders.order_row import OrderRow
from models.customer_orders.product import Product
from models.customer_orders.store import Store


@dataclass(frozen=True)
class CustomerOrdersExtractedData:
    customers: list[Customer]
    orders: list[Order]
    currency_exchanges: list[CurrencyExchange]
    stores: list[Store]
    products: list[Product]
    order_rows: list[OrderRow]