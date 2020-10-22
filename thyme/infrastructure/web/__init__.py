from domain.usecases.tasks import CreateTaskUseCase, DeleteTaskUseCase, GetTasksUseCase
from flask import Flask
from flask_restful import Api
from infrastructure.db.connection import DB
from infrastructure.db.daos import DBTasksDAO
from infrastructure.web.api import ApiTasksResource
from infrastructure.web.config import Config
from infrastructure.web.views import TasksView, TaskView


def create_flask_app(name, thyme_web_app) -> Flask:
    app = Flask(name, template_folder="infrastructure/web/templates")
    api = Api(app, prefix='/api')

    views_kwargs = {"web_app": thyme_web_app}
    add = app.add_url_rule
    add("/", view_func=TasksView.as_view("tasks", **views_kwargs))
    add("/<int:task_id>", view_func=TaskView.as_view("task", **views_kwargs))
    api.add_resource(ApiTasksResource, '/', resource_class_kwargs=views_kwargs)
    return app


class WebApp:
    def __init__(self, name: str, config: Config):
        db = DB(url=config.DATABASE_URL)
        session = db.create_session()
        db_tasks_dao = DBTasksDAO(session=session)

        self.DEBUG = config.DEBUG

        self.get_tasks_usecase = GetTasksUseCase(tasks_dao=db_tasks_dao)
        self.create_tasks_usecase = CreateTaskUseCase(tasks_dao=db_tasks_dao)
        self.delete_task_usecase = DeleteTaskUseCase(tasks_dao=db_tasks_dao)

        self.app = create_flask_app(name, self)

    def run(self):
        self.app.run(host="0.0.0.0", debug=self.DEBUG)


def create_app():
    return WebApp(name="Thyme", config=Config())
