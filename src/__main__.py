import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src import infrastructure
from src.api import controllers, app_factory


def main() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await infrastructure.init_db()
        yield
        await infrastructure.close_db()

    app = app_factory(lifespan=lifespan)
    controllers.setup(app)

    return app


def run():
    settings = infrastructure.settings
    uvicorn.run(
        "src:main",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        factory=settings.FACTORY
    )


if __name__ == "__main__":
    run()
