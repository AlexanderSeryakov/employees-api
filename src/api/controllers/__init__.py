from fastapi import FastAPI

from .employees import employees_router
from .default import default_router


def setup(app: FastAPI):
    app.include_router(default_router)
    app.include_router(employees_router)
