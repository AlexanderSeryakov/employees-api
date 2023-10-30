import beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .models import Employee


class DatabaseClient:
    client: AsyncIOMotorClient = None


db = DatabaseClient()


# ToDo: тут надо сделать импорт url из сеттингов
async def init_db() -> None:
    db.client = AsyncIOMotorClient(
        "mongodb://mongodb:27017"
    )
    await beanie.init_beanie(
        database=db.client.employees_database,
        document_models=[
            Employee
        ]
    )


async def close_db() -> None:
    await db.client.close()
