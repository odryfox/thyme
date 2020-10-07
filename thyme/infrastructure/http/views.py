from flask import render_template, request
from flask.views import MethodView


class TasksView(MethodView):
    def __init__(self, web_app):
        self.web_app = web_app

    def get(self):
        tasks = self.web_app.get_tasks_usecase.execute()
        return render_template("index.html", tasks=tasks)

    def post(self):
        self.web_app.create_tasks_usecase.execute(request.form["name"])
        tasks = self.web_app.get_tasks_usecase.execute()
        return render_template("index.html", tasks=tasks)
