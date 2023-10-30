from typing import Type
from dataclasses import asdict
from src.core import EmployeeDTO
from ..models import Employee


class EmployeeDAO:
    def __init__(self, employee: Type[Employee]) -> None:
        self.employee = employee

    async def get_all(
            self,
            criteria: list = None,
            ordering: str = None,
            limit: int = 20,
            skip: int = 0
    ) -> list[EmployeeDTO]:
        employees = await self.employee.find_many(
            *criteria,
            limit=limit,
            skip=skip,
        ).sort(ordering).to_list()
        result = [EmployeeDTO(**employee.model_dump()) for employee in employees]
        return result

    async def create_one(self, employee_data: EmployeeDTO) -> str:
        created_obj = await self.employee.insert_one(self.employee(**asdict(employee_data)))
        return str(created_obj.id)
