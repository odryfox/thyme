from dataclasses import dataclass
from datetime import date, time


@dataclass
class TaskEntity:
    id: int
    name: str
    status: str
    date_start: date
    time_start: time
