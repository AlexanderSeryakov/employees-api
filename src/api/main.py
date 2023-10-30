from fastapi import FastAPI
from src.infrastructure import settings


def app_factory() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG_MODE,
        docs_url="/api/docs"
    )

    return app
