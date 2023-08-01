from typing import Type

from sqlalchemy import select, func
from assignment.trader.models import Trader, TraderRequestErrors
from core.models.repository import BaseAsyncRepository


class TraderRepository(BaseAsyncRepository[Trader]):

    @property
    def model(self) -> Type[Trader]:
        return Trader


class TraderRequestErrorsRepository(BaseAsyncRepository[TraderRequestErrors]):

    @property
    def model(self) -> Type[TraderRequestErrors]:
        return TraderRequestErrors

    async def count(self) -> int:
        stmt = select(func.count(self.model.id))
        count = await self.session.execute(stmt)
        return count.scalar()
