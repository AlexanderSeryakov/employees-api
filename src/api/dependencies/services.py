from src.infrastructure import EmployeeDAO, Employee
from src.core.services import EmployeeService


def employee_service() -> EmployeeService:
    return EmployeeService(EmployeeDAO(Employee))
