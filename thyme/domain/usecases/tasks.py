from typing import List

from domain.entities import TaskEntity
from domain.interfaces import ITasksDAO


class GetTasksUseCase:
    def __init__(self, tasks_dao: ITasksDAO):
        self.tasks_dao = tasks_dao

    def execute(self) -> List[TaskEntity]:
        tasks = self.tasks_dao.get_list()
        return tasks
