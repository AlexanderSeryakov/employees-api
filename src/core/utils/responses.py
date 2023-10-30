from dataclasses import dataclass

from src.api.shcemas import SEmployee


@dataclass
class EmployeesListResponse:
    count: int
    employees: list[SEmployee]
