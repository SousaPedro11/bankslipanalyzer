from typing import Optional

import pydantic
from decouple import config


class Settings(pydantic.BaseSettings):
    SERVICE_NAME: str = config("SERVICE_NAME", default="bankslip")
    PREFIX: str = config("PREFIX", default=f"/{SERVICE_NAME}/v1")
    PRODUCTION: bool = config("PRODUCTION", default=False, cast=bool)
    DEBUG: bool = config("DEBUG", default=False, cast=bool)

    SENTRY_DSN: Optional[pydantic.HttpUrl] = config("SENTRY_DSN", default=None)

    JWT_EXPIRES_IN_HOURS: int = config("JWT_EXPIRES_IN_HOURS", default=6, cast=int)
    JWT_SECRET: pydantic.SecretStr = config(
        "JWT_SECRET",
        default="969824a6-93e4-11eb-8da1-51115a0d4746",
    )
    PORT: int = config("PORT", default=8000, cast=int)

    class Config:
        env_file = ".env"


settings = Settings()
