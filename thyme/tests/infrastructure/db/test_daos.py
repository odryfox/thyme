from datetime import date, time

from domain.constants import TaskStatusEnum
from infrastructure.db.daos import DBTasksDAO

# pylint: disable=no-self-use


class TestDBTasksDAO:

    def test_create_and_get_tasks(self, db_tasks_dao: DBTasksDAO):
        name = "name"
        status = TaskStatusEnum.created
        date_start = date(2020, 12, 13)
        time_start = time(15, 45, 00)

        db_tasks_dao.create(name=name, status=status, date_start=date_start, time_start=time_start)

        tasks = db_tasks_dao.get_list()

        assert len(tasks) == 1
        assert tasks[0].name == name
        assert tasks[0].status == status
        assert tasks[0].date_start == date_start
        assert tasks[0].time_start == time_start
