from datetime import date, time

from domain.constants import TaskStatusEnum
from domain.interfaces import ITasksDAO
from domain.usecases.tasks import GetTasksUseCase


def test_get_all_tasks_use_case(tasks_dao: ITasksDAO):
    name = "name"
    status = TaskStatusEnum.created
    date_start = date(2020, 12, 13)
    time_start = time(12, 45, 00)

    tasks_dao.create(name=name, status=status, date_start=date_start, time_start=time_start)

    usecase = GetTasksUseCase(tasks_dao=tasks_dao)

    tasks = usecase.execute()

    assert tasks
