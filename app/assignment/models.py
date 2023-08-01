from enum import Enum

from sqlalchemy import String, Float, Integer
from core.models import Base
from core.models.mixins import PersonMixin, NotNullableColumn, PrimaryKeyColumn
from core.models.models import EnumValueType


class TransactionType(str, Enum):
    buy = "buy"
    sell = "sell"


class Trader(Base[int], PersonMixin):
    """
    create a Trader class that inherits from the Person class.
    It should have the following additional attributes: transactionType, assetType, assetValue, and quantity
    """
    id = PrimaryKeyColumn()
    transaction_type = NotNullableColumn(EnumValueType(TransactionType))
    assetType = NotNullableColumn(String(50))
    assetValue = NotNullableColumn(Float)
    quantity = NotNullableColumn(Integer)
