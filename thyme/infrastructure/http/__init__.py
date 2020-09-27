from flask import Flask
from flask_restful import Api
from infrastructure.http.api import ApiTasksResource
from infrastructure.http.views import TasksView


def create_flask_app(name, thyme_web_app) -> Flask:
    app = Flask(name, template_folder="infrastructure/http/templates")
    api = Api(app, prefix='/api')

    views_kwargs = {"web_app": thyme_web_app}
    add = app.add_url_rule
    add("/", view_func=TasksView.as_view("tasks", **views_kwargs))
    api.add_resource(ApiTasksResource, '/', resource_class_kwargs=views_kwargs)
    return app
