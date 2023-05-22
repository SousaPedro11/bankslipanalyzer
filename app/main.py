from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.helpers.handler import register_exception_handlers
from app.api.router import api_router
from app.settings import settings
from bank_return.app.api.router import return_router
from bank_shipping.app.api.router import shipping_router
from bank_slip.app.api.router import bank_slip_router


def get_app() -> FastAPI:
    """
    Create and configure an instance of the FastAPI application.
    :return: a FastAPI application instance
    """
    app = FastAPI(
        title="Bank Slip Analyzer API",
        version="1.0.0",
        description="This is a simple API to analyze bank slips",
        openapi_url=f"{settings.PREFIX}/openapi.json" if not settings.PRODUCTION else None,
        docs_url=f"{settings.PREFIX}/docs" if not settings.PRODUCTION else None,
        redoc_url=f"{settings.PREFIX}/redoc" if not settings.PRODUCTION else None,
        contact={
            "name": "Sousa & Sousa Software Development Ltda",
            "email": "sousapedro11.ti@gmail.com",
        },
    )

    app.add_middleware(
        CORSMiddleware,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_exception_handlers(app)

    app.include_router(api_router, prefix=settings.PREFIX)
    app.include_router(bank_slip_router, prefix=settings.PREFIX)
    app.include_router(shipping_router, prefix=settings.PREFIX)
    app.include_router(return_router, prefix=settings.PREFIX)

    if settings.SENTRY_DSN:
        import sentry_sdk
        from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

        sentry_sdk.init(settings.SENTRY_DSN, traces_sample_rate=1.0)
        app.add_middleware(SentryAsgiMiddleware)
    return app
