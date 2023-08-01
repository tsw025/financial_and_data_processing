from pydantic import BaseModel, Field

from assignment.models import TransactionType


class TraderBase(BaseModel):
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
