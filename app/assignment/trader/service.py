from fastapi import Depends

from assignment.trader.models import Trader
from assignment.trader.repository import TraderRepository
from assignment.trader.schema import TraderRequest, TraderResponse


class TraderService:

    def __init__(self, trader_repo: TraderRepository = Depends()):
        self.trader_repo = trader_repo

    async def create(self, trader_req: TraderRequest) -> TraderResponse:
        trader = Trader(**trader_req.model_dump(exclude_unset=True))
        await self.trader_repo.add(
            trader
        )
        await self.trader_repo.commit()
        await self.trader_repo.session.refresh(trader)
        return TraderResponse.model_validate(trader)
