from typing import Type

from assignment.trader.models import Trader
from core.models.repository import BaseAsyncRepository


class TraderRepository(BaseAsyncRepository[Trader]):

    @property
    def model(self) -> Type[Trader]:
        return Trader
