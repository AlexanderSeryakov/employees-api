import beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .models import Employee
from src.infrastructure import settings


class DatabaseClient:
    client: AsyncIOMotorClient = None


db = DatabaseClient()

if settings.MODE == "TEST":
    db_url = settings.TEST_DB_URL
else:
    db_url = settings.DB_URL


async def init_db() -> None:
    db.client = AsyncIOMotorClient(
        db_url
    )
    await beanie.init_beanie(
        database=db.client.test_db if settings.MODE == "TEST" else db.client.employees_database,
        document_models=[
            Employee
        ]
    )


async def close_db() -> None:
    await db.client.close()
