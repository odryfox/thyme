from flask import Flask

from infrastructure.db.daos import MockNewsDAO
from infrastructure.http.api import NewsView
from domain.usecases.news import GetNewsUseCase


class WebApp:
    def __init__(self, name: str):
        self.app = Flask(name)
        self.news_dao = MockNewsDAO()
        self.get_news_usecase = GetNewsUseCase(news_dao=self.news_dao)

        views_kwargs = {"web_app": self}
        add = self.app.add_url_rule
        add('/', view_func=NewsView.as_view("name", **views_kwargs))

    def run(self):
        self.app.run()
