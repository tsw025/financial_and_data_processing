from datetime import datetime

from pydantic import BaseModel, Field

from core.schema.fields import NAME_PATTERN


class OrmBase(BaseModel):
    """Base class for all ORM models."""

    class Config:
        """Config."""

        # orm_mode = True
        from_attributes = True


class Person(BaseModel):
    name: str = Field(pattern=NAME_PATTERN, example="John Doe", max_items=100, min_items=1)


class Timestamp(BaseModel):
    created_at: datetime = Field(readOnly=True)
    updated_at: datetime = Field(readOnly=True)
