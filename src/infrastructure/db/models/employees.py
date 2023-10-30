from datetime import datetime
from decimal import Decimal
from typing import Annotated, Any

from bson import Decimal128

from beanie import Document
from pydantic import Field, model_validator


class Employee(Document):
    name: str
    email: str
    age: int = Field(gt=0, lt=200)
    company: str
    # ToDo: формат даты нужно обговорить заранее с командой/клиентом, по умолчанию делаю utcnow
    join_date: datetime = Field(default_factory=datetime.utcnow)
    job_title: str
    gender: str
    salary: Annotated[Decimal, Field(decimal_places=2)]

    @model_validator(mode="before")
    @classmethod
    def convert_bson_decimal128_to_decimal(cls, data: dict[str, Any]) -> Any:
        # ToDo: сейчас есть проблема с работой
        #  Pydantic и Beanie по части Decimal, это временное решение
        for field in data:
            if isinstance(data[field], Decimal128):
                data[field] = data[field].to_decimal()
        return data

    class Settings:
        name = "employees"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@gmail.com",
                "age": 28,
                "company": "Plarin",
                "join_date": "2003-12-28T18:18:10-08:00",
                "job_title": "Developer",
                "gender": "male",
                "salary": 10000
            }
        }
