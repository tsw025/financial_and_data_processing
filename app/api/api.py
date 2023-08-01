from fastapi import APIRouter
from .endpoints import trader

api_router = APIRouter()

api_router.include_router(
    trader.router,
    prefix="/trader",
)
