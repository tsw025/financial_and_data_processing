from typing import Any

from pydantic import Field, BaseModel

from assignment.trader.models import TransactionType
from core.schema import base as base_schema


class TraderBase(base_schema.Person):
    """
    Trader Base.

        transactionType should be either "buy" or "sell".
        assetValue should be a non-negative float.
        quantity should be a non-negative integer.
    """
    transaction_type: TransactionType
    assetType: str = Field(max_length=50)
    assetValue: float = Field(ge=0)
    quantity: int = Field(ge=0)


class TraderResponse(base_schema.OrmBase, TraderBase, base_schema.Timestamp):
    id: int


class TraderRequest(TraderBase):
    pass


class TraderRequestWithoutValidation(TraderRequest):
    transaction_type: Any
    assetType: Any
    assetValue: Any
    quantity: Any
    name: Any
