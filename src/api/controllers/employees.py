from dataclasses import asdict
from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import employee_service
from src.core import EmployeesListResponse, EmployeesFilterArgs
from src.core.services import EmployeeService
from src.api.shcemas import SEmployee


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
