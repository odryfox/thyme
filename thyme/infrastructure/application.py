from domain.usecases.news import GetNewsUseCase
from infrastructure.config import Config
from infrastructure.db.connection import DB
from infrastructure.db.daos import DBNewsDAO
from infrastructure.http import create_flask_app


class WebApp:
    def __init__(self, name: str, config: Config):
        db = DB(url=config.DATABASE_URL)
        session = db.create_session()
        db_news_dao = DBNewsDAO(session=session)

        self.DEBUG = config.DEBUG

        self.get_news_usecase = GetNewsUseCase(news_dao=db_news_dao)

        self.app = create_flask_app(name, self)

    def run(self):
        self.app.run(host="0.0.0.0", debug=self.DEBUG)


def create_web_app():
    return WebApp(name="Thyme", config=Config())
