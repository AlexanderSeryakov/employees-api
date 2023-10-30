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
    # ToDo: в проде salary обычно Decimal,
    #  возможно стоит оставить int по согласованию с командой/клиентом
    salary: Decimal
    id: str = None
    revision_id: str = None
