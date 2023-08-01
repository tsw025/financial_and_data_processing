from datetime import datetime

from pydantic import BaseModel, Field


class OrmBase(BaseModel):
    """Base class for all ORM models."""

    class Config:
        """Config."""

        orm_mode = True


class TimeStamp(BaseModel):
    """Base class for all models with timestamp fields."""

    created_at: datetime = Field(readOnly=True)
    updated_at: datetime = Field(readOnly=True)
