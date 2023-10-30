from dataclasses import asdict
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from src.api.dependencies import employee_service
from src.core import EmployeesListResponse, EmployeesFilterArgs
from src.core.services import EmployeeService
from src.infrastructure import Employee, EmployeeDAO
from src.api.shcemas import SEmployeeInput, SEmployee


employees_router = APIRouter(
    prefix="/api/v1/employees"
)


@employees_router.get("")
async def get_employees(
        service: Annotated[EmployeeService, Depends(employee_service)],
        filters: EmployeesFilterArgs = Depends()
) -> EmployeesListResponse:
    employees = await service.get_employees_for_criteria(criteria=filters)
    employees_to_response = [SEmployee(**asdict(employee)) for employee in employees]
    return EmployeesListResponse(
        count=len(employees_to_response),
        employees=employees_to_response
    )


@employees_router.post("", status_code=status.HTTP_201_CREATED)
async def create_employer(employer: SEmployeeInput) -> dict[str, str]:
    created_employee_id = await EmployeeDAO(Employee).create_one(employer.to_dto())
    return {"employee_id": created_employee_id}

