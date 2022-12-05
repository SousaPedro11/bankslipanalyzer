import uvicorn


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "app.main:get_app",
        reload=True,
        factory=True,
    )


if __name__ == "__main__":
    main()
