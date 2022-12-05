from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.settings import settings


def get_app():
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
            "name": "Desenvolvimento Koper",
            "url": "https://koper.com.br/",
        },
    )

    app.add_middleware(
        CORSMiddleware,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.PREFIX)

    if settings.SENTRY_DSN:
        import sentry_sdk
        from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

        sentry_sdk.init(settings.SENTRY_DSN, traces_sample_rate=1.0)
        app.add_middleware(SentryAsgiMiddleware)
    return app
