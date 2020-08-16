from domain.usecases.news import GetNewsUseCase
from infrastructure.db.connection import create_session
from infrastructure.db.daos import MockNewsDAO, DBNewsDAO
from infrastructure.http import create_flask_app


class WebApp:
    def __init__(self, name: str):
        database_url = "postgresql://localhost/thyme"
        session = create_session(url=database_url)
        DBNewsDAO(session=session)

        news_dao = MockNewsDAO()
        self.get_news_usecase = GetNewsUseCase(news_dao=news_dao)

        self.app = create_flask_app(name, self)

    def run(self):
        self.app.run(host="0.0.0.0")


def create_web_app():
    return WebApp(name="Thyme")
