from src.core import EmployeesFilterArgs
from src.infrastructure import EmployeeDAO


class EmployeeService:
    def __init__(self, dao: EmployeeDAO):
        self.dao = dao

    async def get_employees_for_criteria(self, criteria: EmployeesFilterArgs, ):
        order, filters = criteria.prepare_filters()
        result = await self.dao.get_all(
            criteria=filters,
            ordering=order,
            limit=criteria.limit,
            skip=criteria.skip
        )
        return result
