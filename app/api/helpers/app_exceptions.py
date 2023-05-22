from fastapi import Request
from starlette.responses import JSONResponse

from app.api.helpers.mapper import CODE_ERRORS


class AppExceptionCaseError(Exception):
    def __init__(self, code: int, message: str) -> None:
        self.exception_case = self.__class__.__name__
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"<AppException {self.exception_case} - status_code={self.code} - context={self.message}>"


async def app_exception_handler(_: Request, exc: AppExceptionCaseError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.code,
        content={
            "code": CODE_ERRORS.get(exc.code, exc.code),
            "message": exc.message,
        },
    )


class AppException:
    class InternalError(AppExceptionCaseError):
        """
        Any internal Error
        """

        def __init__(self, message: str = "An unexpected error occurred") -> None:
            status_code = 500
            AppExceptionCaseError.__init__(self, status_code, message)

    class NotFoundError(AppExceptionCaseError):
        """
        Item Not Found
        """

        def __init__(self, message: str) -> None:
            status_code = 404
            AppExceptionCaseError.__init__(self, status_code, message)

    class RequiresAuthError(AppExceptionCaseError):
        """
        Is not public and requires auth
        """

        def __init__(self, message: str) -> None:
            status_code = 401
            AppExceptionCaseError.__init__(self, status_code, message)

    class ForbiddenError(AppExceptionCaseError):
        """
        Is not public and requires auth
        """

        def __init__(self, message: str) -> None:  # pragma: no cover
            status_code = 403
            AppExceptionCaseError.__init__(self, status_code, message)
