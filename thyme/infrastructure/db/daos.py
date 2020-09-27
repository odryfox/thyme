from datetime import date, time
from typing import List

from domain.entities import TaskEntity
from domain.interfaces import ITasksDAO
from infrastructure.db.models import TaskORM
from sqlalchemy.orm import Session


class DBTasksDAO(ITasksDAO):
    def __init__(self, session: Session):
        self.session = session

    def _task_orm_to_entity(self, task_orm: TaskORM):
        return TaskEntity(
            id=task_orm.id,
            name=task_orm.name,
            status=task_orm.status,
            date_start=task_orm.date_start,
            time_start=task_orm.time_start,
        )

    def get_list(self) -> List[TaskEntity]:
        tasks_orm = self.session.query(TaskORM).all()
        task_entities = [self._task_orm_to_entity(task_orm) for task_orm in tasks_orm]
        return task_entities

    def create(self, name: str, status: str, date_start: date, time_start: time) -> TaskEntity:
        task_orm = TaskORM(name=name, status=status, date_start=date_start, time_start=time_start)
        self.session.add(task_orm)
        self.session.commit()
        task_entity = self._task_orm_to_entity(task_orm)
        return task_entity
