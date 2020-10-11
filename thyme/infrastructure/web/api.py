from flask_restful import Resource
from infrastructure.web.serializers import tasks_schema


class ApiTasksResource(Resource):
    def __init__(self, web_app):
        self.web_app = web_app

    def get(self):
        tasks = self.web_app.get_tasks_usecase.execute()
        return tasks_schema.dump(tasks)
