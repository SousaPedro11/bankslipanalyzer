import uvicorn

from app.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "app.main:get_app",
        reload=True,
        factory=True,
        host=settings.HOST,
        port=settings.PORT,
    )


if __name__ == "__main__":
    main()
