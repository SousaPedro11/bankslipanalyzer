import logging

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.api.helpers.mapper import CODE_ERRORS

logger = logging.getLogger("financial")


async def http_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
    logger.error(exc.__dict__)

    return JSONResponse(
        content={"code": CODE_ERRORS.get(exc.status_code, exc.status_code), "message": exc.detail},
        status_code=exc.status_code,
    )


async def request_validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    logger.error(exc.__dict__)

    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "code": CODE_ERRORS.get(422, 422),
            "message": "Campos inválidos",
            "detail": jsonable_encoder(exc.errors()),
        },
    )
