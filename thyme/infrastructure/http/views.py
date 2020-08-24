from flask import render_template
from flask.views import MethodView


class NewsView(MethodView):
    def __init__(self, web_app):
        self.web_app = web_app

    def get(self):
        news = self.web_app.get_news_usecase.execute()
        return render_template("index.html", news=news)
