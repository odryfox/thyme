from flask import render_template, request
from flask.views import MethodView


class TasksView(MethodView):
    def __init__(self, web_app):
        self.web_app = web_app
        super().__init__()

    def get(self):
        tasks = self.web_app.get_tasks_usecase.execute()
        return render_template("index.html", tasks=tasks)

    def post(self):
        self.web_app.create_tasks_usecase.execute(request.form["name"])
        tasks = self.web_app.get_tasks_usecase.execute()
        return render_template("index.html", tasks=tasks)


class TaskView(MethodView):
    def __init__(self, web_app):
        self.web_app = web_app
        super().__init__()

    def post(self, task_id):
        self.web_app.delete_task_usecase.execute(task_id=task_id)
        tasks = self.web_app.get_tasks_usecase.execute()
        return render_template("index.html", tasks=tasks)

    def put(self, task_id):
        status = request.json["status"]
        self.web_app.update_task_usecase.execute(task_id=task_id, status=status)
        return "OK"
