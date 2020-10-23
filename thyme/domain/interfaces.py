from abc import ABC, abstractmethod
from datetime import date, time
from typing import List

from domain.constants import TaskStatusEnum
from domain.entities import TaskEntity


class ITasksDAO(ABC):

    @abstractmethod
    def get_list(self) -> List[TaskEntity]:
        pass

    @abstractmethod
    def create(self, name: str, status: TaskStatusEnum, date_start: date, time_start: time) -> TaskEntity:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> None:
        pass

    @abstractmethod
    def update(self, task_id: int, status: TaskStatusEnum) -> None:
        pass
