import abc
from typing import Any, Generic, List, Optional, Type, TypeVar

from fastapi import Depends
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_async_session
from core.models import models

T = TypeVar("T", bound=models.Base)


class BaseAsyncRepository(abc.ABC, Generic[T]):
    """Base class for implementing async repositories."""

    @property
    @abc.abstractmethod
    def model(self) -> Type[T]:
        """Used in functions calls to construct a session based on the SQLAlchemy model."""
        raise NotImplementedError("This function needs to be implemented in derived classes.")

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        """Init. the base class."""
        self._session = session

    @property
    def session(self) -> AsyncSession:
        """Used to get the session, for example to commit changes."""
        return self._session

    async def commit(self):
        """Persist all changes in the session."""
        return await self.session.commit()

    async def find(self, **filter_options) -> List[T]:
        """Find an entity by supplying a filter statement."""
        stmt = select(self.model).filter_by(**filter_options)
        results = await self.session.execute(stmt)
        return results.scalars().all()

    async def filter(self, **filter_options) -> List[T]:
        """Find an entity by supplying a filter statement."""
        stmt = select(self.model).filter_by(**filter_options)
        results = await self.session.execute(stmt)
        return results.scalars().all()

    async def find_one(self, **filter_options) -> Optional[T]:
        """Find one entity by supplying a filter statement."""
        stmt = select(self.model).filter_by(**filter_options)
        results = await self.session.execute(stmt)
        return results.scalars().first()

    async def find_by_id(self, identity: Any) -> Optional[T]:
        """Find an entity by identity."""
        return await self.session.get(self.model, identity)

    async def find_all(self) -> List[T]:
        """Get all entities."""
        results = await self.session.execute(select(self.model).order_by(self.model.id))
        return results.scalars().all()

    async def add(self, entity: T, flush: bool = True):
        self.session.add(entity)
        if flush:
            await self.session.flush()

    async def update(self, identity: Any, **values: Any):
        """Update an entity with supplied values."""
        stmt = update(self.model).filter_by(**{"id": identity}).values(**values)
        await self.session.execute(stmt)

    async def delete(self, identity: Any):
        """Delete an object."""
        stmt = delete(self.model).filter_by(**{"id": identity})
        await self.session.execute(stmt)

    async def delete_by_filter_options(self, **filter_options):
        """Delete an object by filter options."""
        stmt = select(self.model).filter_by(**filter_options)
        result = await self.session.execute(stmt)
        result_to_delete = result.scalars().one()
        await self.session.delete(result_to_delete)

    async def delete_by_ids(self, identities: List[Any]):
        """Bulk delete objects by supplying a list of identities."""
        stmt = delete(self.model).where(self.model.id.in_(identities))  # type: ignore
        await self.session.execute(stmt)
