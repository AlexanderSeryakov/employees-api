import uvicorn
from fastapi import FastAPI

from src import infrastructure
from src.api import controllers, app_factory


def main() -> FastAPI:
    app = app_factory()

    @app.on_event("startup")
    async def init_database():
        await infrastructure.init_db()

    @app.on_event("shutdown")
    async def close_connection():
        await infrastructure.close_db()

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
