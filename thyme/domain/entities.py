from dataclasses import dataclass
from datetime import date, time

from domain.constants import TaskStatusEnum


@dataclass
class TaskEntity:
    id: int
    name: str
    status: TaskStatusEnum
    date_start: date
    time_start: time
