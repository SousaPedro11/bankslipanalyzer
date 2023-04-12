from fastapi import Request
from starlette.responses import JSONResponse

from app.api.helpers.mapper import CODE_ERRORS


class AppExceptionCase(Exception):
    def __init__(self, code: int, message: str):
        self.exception_case = self.__class__.__name__
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"<AppException {self.exception_case} - " + f"status_code={self.code} - context={self.message}>"


async def app_exception_handler(_: Request, exc: AppExceptionCase) -> JSONResponse:
    return JSONResponse(
        status_code=exc.code,
        content={
            "code": CODE_ERRORS.get(exc.code, exc.code),
            "message": exc.message,
        },
    )


class AppException:
    class InternalError(AppExceptionCase):
        """
        Any internal Error
        """

        def __init__(self, message: str = "An unexpected error occurred"):
            status_code = 500
            AppExceptionCase.__init__(self, status_code, message)

    class NotFoundError(AppExceptionCase):
        """
        Item Not Found
        """

        def __init__(self, message: str):
            status_code = 404
            AppExceptionCase.__init__(self, status_code, message)

    class RequiresAuthError(AppExceptionCase):
        """
        Is not public and requires auth
        """

        def __init__(self, message: str):
            status_code = 401
            AppExceptionCase.__init__(self, status_code, message)

    class ForbiddenError(AppExceptionCase):
        """
        Is not public and requires auth
        """

        def __init__(self, message: str):  # pragma: no cover
            status_code = 403
            AppExceptionCase.__init__(self, status_code, message)
