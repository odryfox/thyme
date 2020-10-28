from typing import Any, Type

from domain.constants import TaskStatusEnum
from sqlalchemy import Column, Date, Enum, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base

Base: Any = declarative_base()


class TaskORM(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    status = Column(Enum(TaskStatusEnum), nullable=False)

    date_start = Column(Date, nullable=False)
    time_start = Column(Time, nullable=False)

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.name.__repr__()}, status={self.status.__repr__()}, " \
               f"date_start={self.date_start.__repr__()}, time_start={self.time_start.__repr__()})>"
