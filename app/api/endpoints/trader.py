from fastapi import APIRouter, status, Depends

from assignment.trader.queue_service_imp import DataAnalyserQueueService
from assignment.trader.schema import TraderResponse, TraderRequestWithoutValidation, DataAnalyserResponse
from assignment.trader.service import TraderService

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TraderResponse)
async def create_trade(
        trader: TraderRequestWithoutValidation,
        service: TraderService = Depends(),
) -> TraderResponse:
    return await service.create(trader)


@router.get("/errors/count", status_code=status.HTTP_200_OK, response_model=int)
async def get_errors_count(
        service: TraderService = Depends(),
):
    return await service.get_errors_count()


@router.post("-queue", status_code=status.HTTP_201_CREATED, response_model=TraderResponse)
async def create_trade(
        trader: TraderRequestWithoutValidation,
        service: DataAnalyserQueueService = Depends(),
) -> TraderResponse:
    return await service.create(trader)


@router.post("/analyse", status_code=status.HTTP_200_OK)
def analyse(
        service: DataAnalyserQueueService = Depends(),
):
    return service.start_analysis()
