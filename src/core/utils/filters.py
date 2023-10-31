from decimal import Decimal
from typing import Annotated, Any

from fastapi import Query
from .constants import ALL_FILTERS_FIELD, STR_MATCHING_FILTERS_FIELD, ORDER_TYPES


class Paginator:
    def __init__(self, limit: int = 10, skip: int = 0) -> None:
        self.limit = limit
        self.skip = skip


class EmployeesFilterArgs(Paginator):
    # ToDo: это всё нужно переделывать :) по-хорошему фильтры и константы нужно выносить
    #  в domain-слой и чтобы либы/фреймворк туда не протекали
    def __init__(
            self,
            name: Annotated[str, Query(description="Фильтр по имени сортудника")] = None,
            email: Annotated[str, Query(description="Фильтр по e-mail сотрудника")] = None,
            company: Annotated[str, Query(max_length=64, description="Фильтр по имени компании")] = None,
            job_title: Annotated[str, Query(max_length=64, description="Фильтр по должности")] = None,
            gender: Annotated[str, Query(
                description="Фильтр по полу: female | male | other")
            ] = None,
            age: Annotated[int, Query(gt=0, description="Сотрудники, с указанным возрастом и меньше")] = None,
            salary: Annotated[Decimal, Query(
                decimal_places=2, description="Уровень зарплаты сотрудника меньше, чем")
            ] = None,
            limit: Annotated[int, Query(gt=0, lt=500, description="Вывести записей")] = 10,
            skip: Annotated[int, Query(ge=0, description="Начать с записи")] = 0,
            order: Annotated[str, Query(
                description="Порядок сортировки: age | name | salary. Для обратной сортировки: -age")
            ] = None
    ) -> None:
        super().__init__(limit, skip)
        self.name = name
        self.email = email
        self.age = age
        self.company = company
        self.job_title = job_title
        self.gender = gender
        self.salary = salary
        self.order = order

    def prepare_filters(self) -> tuple[Any, list[dict]]:
        # ToDo: добавить {"age": {"$gt": current_filter_value}} и аналогично для salary,
        #  чтобы можно было фильтровать не только кейс, где age/salary меньше указанных, но и наоборот.
        #  Также можно сделать что-то типо Query-билдера и вынести его в отдельную сущность,
        #  чтобы не писать "сырые" запросы
        choice_filters = []
        order = "name"
        for filter_name in ALL_FILTERS_FIELD:
            current_filter_value = getattr(self, filter_name)
            match filter_name:
                case str() as f_name if filter_name in STR_MATCHING_FILTERS_FIELD:
                    if current_filter_value:
                        choice_filters.append({f_name: {"$regex": f"^{current_filter_value}"}})
                case "age":
                    if current_filter_value:
                        choice_filters.append({"age": {"$lt": current_filter_value + 1}})
                case "salary":
                    if current_filter_value:
                        choice_filters.append({"salary": {"$lt": current_filter_value}})

        choice_order = getattr(self, "order")
        if choice_order in ORDER_TYPES:
            order = choice_order

        return order, choice_filters
