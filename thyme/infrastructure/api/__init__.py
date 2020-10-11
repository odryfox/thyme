from domain.usecases.tasks import CreateTaskUseCase, GetTasksUseCase
from fastapi import FastAPI
from infrastructure.api.config import Config
from infrastructure.db.connection import DB
from infrastructure.db.daos import DBTasksDAO


def create_fast_api_app(name, thyme_api_app):
    app = FastAPI()
    return app


class APIApp:
    def __init__(self, name: str, config: Config):
        db = DB(url=config.DATABASE_URL)
        session = db.create_session()
        db_tasks_dao = DBTasksDAO(session=session)

        self.DEBUG = config.DEBUG

        self.get_tasks_usecase = GetTasksUseCase(tasks_dao=db_tasks_dao)
        self.create_tasks_usecase = CreateTaskUseCase(tasks_dao=db_tasks_dao)

        self.app = create_fast_api_app(name, self)


def create_app():
    return APIApp(name="Thyme api", config=Config())
