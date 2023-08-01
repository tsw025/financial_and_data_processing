from fastapi import APIRouter, status, Depends
from assignment.trader.schema import TraderResponse, TraderRequest
from assignment.trader.service import TraderService

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TraderResponse)
async def create_trade(
        trader: TraderRequest,
        service: TraderService = Depends(),
) -> TraderResponse:
    return await service.create(trader)
