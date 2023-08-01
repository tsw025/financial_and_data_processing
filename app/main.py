from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from api.api import api_router
from assignment.trader.exceptions import TraderServiceValidationException

app = FastAPI(
    titile="Financial and Data Processing",
)

app.include_router(api_router)


# Exception handling
@app.exception_handler(TraderServiceValidationException)
async def db_record_not_found_handler(request: Request, exception: TraderServiceValidationException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=jsonable_encoder(exception.message))

