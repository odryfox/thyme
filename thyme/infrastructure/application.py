from domain.usecases.tasks import CreateTaskUseCase, GetTasksUseCase
from infrastructure.config import Config
from infrastructure.db.connection import DB
from infrastructure.db.daos import DBTasksDAO
from infrastructure.http import create_flask_app


class WebApp:
    def __init__(self, name: str, config: Config):
        db = DB(url=config.DATABASE_URL)
        session = db.create_session()
        db_tasks_dao = DBTasksDAO(session=session)

        self.DEBUG = config.DEBUG

        self.get_tasks_usecase = GetTasksUseCase(tasks_dao=db_tasks_dao)
        self.create_tasks_usecase = CreateTaskUseCase(tasks_dao=db_tasks_dao)

        self.app = create_flask_app(name, self)

    def run(self):
        self.app.run(host="0.0.0.0", debug=self.DEBUG)


def create_web_app():
    return WebApp(name="Thyme", config=Config())
