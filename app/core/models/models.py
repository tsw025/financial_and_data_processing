"""
Initial setup for the models module.

The models module contains the base model for all models in the application.
Further it contains the utc_now function which is used to generate a timestamp
for the created_at and updated_at columns.

"""
from typing import Generic, TypeVar

from sqlalchemy import DATETIME, MetaData, types
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base
from sqlalchemy.sql import functions

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

ID = TypeVar("ID")


@as_declarative()
class Base(Generic[ID]):
    """Declarative base with auto table name."""

    id: ID
    __name__: str

    metadata = MetaData()

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generate a table name based on where the model is declared.

        :return: a name that follows the structure of classname
        """
        return cls.__name__.lower()


Base = declarative_base(cls=Base, metadata=meta)


class utc_now(functions.GenericFunction):
    """Default generic timestamp function."""

    type = DATETIME()
    inherit_cache = True


# This is a way to add a function to the database that is not supported by
# sqlalchemy. Further it displays the creation for different databases.
@compiles(utc_now, "postgresql")
def pg_utc_now(element, compiler, **kwargs):
    """Returns utc timestamp statement postgresql."""
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(utc_now, "sqlite")
def sqlite_utc_now(element, compiler, **kwargs):
    """Returns utc timestamp statement sqlite."""
    return "datetime('now')"


# configure EnumValueType
class EnumValueType(types.TypeDecorator):
    """Enum SqlAlchemy Type."""

    impl = types.String()
    cache_ok = True

    def __init__(self, enum, *args, **kwargs):
        """Init."""
        self.enum = enum
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, _):
        """
        Process bind param.

        This method is called when a value is being inserted or updated.
        The value is saved as the enum value.

        """
        if value is None:
            return value

        if isinstance(value, self.enum):
            return value.value

        return value

    def process_result_value(self, value, _):
        """Process result value."""
        if value is None:
            return value

        return self.enum(value)

    def copy(self, **kw):
        """Copy."""
        return EnumValueType(self.enum, **kw)
