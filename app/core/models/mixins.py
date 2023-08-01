import datetime
from typing import Type

from sqlalchemy import Column, DateTime, Integer, String
from functools import partial
from sqlalchemy.orm import declarative_mixin

from .models import utc_now


@declarative_mixin
class Timestamp:
    """Adds `created` and `updated` columns to a derived declarative model."""

    created_at: datetime = Column(DateTime, default=None, server_default=utc_now())
    updated_at: datetime = Column(
        DateTime, default=None, server_default=utc_now(), onupdate=utc_now()
    )


def set_primary_key(**kwargs):
    """Helper function for declaring a primary key on a model."""
    return Column(Integer, primary_key=True, **kwargs)


PrimaryKeyColumn = set_primary_key
NotNullableColumn: Type[Column] = partial(Column, nullable=False)


@declarative_mixin
class PersonMixin:
    name = NotNullableColumn(String(50))
