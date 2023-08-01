from fastapi import Depends
from pydantic import ValidationError

from assignment.trader.exceptions import TraderServiceValidationException
from assignment.trader.models import Trader, TraderRequestErrors
from assignment.trader.repository import TraderRepository, TraderRequestErrorsRepository
from assignment.trader.schema import TraderRequest, TraderResponse, TraderRequestWithoutValidation


class TraderService:

    def __init__(self,
                 trader_repo: TraderRepository = Depends(),
                 trader_req_errors_repo: TraderRequestErrorsRepository = Depends()
                 ):
        self.trader_repo = trader_repo
        self.trader_req_errors_repo = trader_req_errors_repo

    async def create(self, trader_req: TraderRequestWithoutValidation) -> TraderResponse:
        try:
            trader_req = TraderRequest(**trader_req.model_dump(exclude_unset=True))
        except ValidationError as e:
            await self.trader_req_errors_repo.add(
                TraderRequestErrors(
                    error=e.json()
                )
            )
            await self.trader_req_errors_repo.commit()
            raise TraderServiceValidationException(e.errors())
        trader = Trader(**trader_req.model_dump(exclude_unset=True))
        await self.trader_repo.add(
            trader
        )
        await self.trader_repo.commit()
        await self.trader_repo.session.refresh(trader)
        return TraderResponse.model_validate(trader)

    async def get_errors_count(self) -> int:
        return await self.trader_req_errors_repo.count()
