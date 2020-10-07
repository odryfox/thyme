from datetime import date, datetime, time
from typing import List

from domain.constants import TaskStatusEnum
from domain.entities import TaskEntity
from domain.interfaces import ITasksDAO


class GetTasksUseCase:
    def __init__(self, tasks_dao: ITasksDAO):
        self.tasks_dao = tasks_dao

    def execute(self) -> List[TaskEntity]:
        tasks = self.tasks_dao.get_list()
        return tasks


class CreateTaskUseCase:
    def __init__(self, tasks_dao: ITasksDAO):
        self.tasks_dao = tasks_dao

    def execute(self, name: str) -> TaskEntity:
        now = datetime.now()
        task = self.tasks_dao.create(
            name=name, status=TaskStatusEnum.created,
            date_start=now.today(), time_start=now.time(),
        )
        return task
