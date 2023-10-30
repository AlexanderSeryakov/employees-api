from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class EmployeeDTO:
    name: str
    email: str
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: str
    # ToDo: в проде salary это всегда Decimal,
    #  но у нас дамп из int, поэтому оставлю int
    salary: Decimal
    id: str = None
    revision_id: str = None
