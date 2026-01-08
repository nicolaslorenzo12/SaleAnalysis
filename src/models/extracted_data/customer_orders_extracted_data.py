from dataclasses import dataclass

from models.raw.raw_currency_exchange import RawCurrencyExchange
from models.raw.raw_customer import RawCustomer
from models.raw.raw_order import RawOrder
from models.raw.raw_order_row import RawOrderRow
from models.raw.raw_product import RawProduct
from models.raw.raw_store import RawStore


@dataclass(frozen=True)
class CustomerOrdersExtractedData:
    customers: list[RawCustomer]
    orders: list[RawOrder]
    currency_exchanges: list[RawCurrencyExchange]
    stores: list[RawStore]
    products: list[RawProduct]
    order_rows: list[RawOrderRow]