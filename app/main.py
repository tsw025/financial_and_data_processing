from fastapi import FastAPI

from api.api import api_router

app = FastAPI(
    titile="Financial and Data Processing",
)

app.include_router(api_router)
