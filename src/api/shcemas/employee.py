from datetime import datetime
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field

from src.core import EmployeeDTO


class SEmployeeInput(BaseModel):
    name: str
    email: str
    age: Annotated[int, Field(gt=0, lt=200)]
    company: str
    join_date: datetime
    job_title: str
    gender: str
    salary: Annotated[Decimal, Field(decimal_places=2)]

    def to_dto(self) -> EmployeeDTO:
        return EmployeeDTO(
            name=self.name,
            email=self.email,
            age=self.age,
            company=self.company,
            join_date=self.join_date,
            job_title=self.job_title,
            gender=self.gender,
            salary=self.salary
        )


class SEmployee(BaseModel):
    id: str
    name: str
    email: str
    age: Annotated[int, Field(gt=0, lt=200)]
    company: str
    join_date: datetime
    job_title: str
    gender: str
    salary: Annotated[Decimal, Field(decimal_places=2)]
