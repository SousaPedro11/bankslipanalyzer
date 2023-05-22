from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.api.helpers.app_exceptions import AppExceptionCaseError, app_exception_handler
from app.api.helpers.request_exceptions import http_exception_handler, request_validation_exception_handler


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    @app.exception_handler(ValidationError)
    async def custom_validation_exception_handler(request: Request, e: RequestValidationError) -> JSONResponse:
        return await request_validation_exception_handler(request, e)

    @app.exception_handler(AppExceptionCaseError)
    async def custom_app_exception_handler(request: Request, e: AppExceptionCaseError) -> JSONResponse:
        return await app_exception_handler(request, e)

    @app.exception_handler(HTTPException)
    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request: Request, e: HTTPException) -> JSONResponse:
        return await http_exception_handler(request, e)
