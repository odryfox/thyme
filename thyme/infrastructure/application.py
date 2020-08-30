from domain.usecases.news import GetNewsUseCase, ImportNewsUseCase
from infrastructure.config import Config
from infrastructure.db.connection import DB
from infrastructure.db.daos import DBNewsDAO
from infrastructure.external.news_import_daos import ExternalNewsAPIDAO
from infrastructure.http import create_flask_app


class WebApp:
    def __init__(self, name: str, config: Config):
        db = DB(url=config.DATABASE_URL)
        session = db.create_session()
        db_news_dao = DBNewsDAO(session=session)
        external_news_api_dao = ExternalNewsAPIDAO(api_key=config.NEWS_API_KEY)

        self.DEBUG = config.DEBUG

        self.get_news_usecase = GetNewsUseCase(news_dao=db_news_dao)
        self.news_api_import_usecase = ImportNewsUseCase(news_dao=db_news_dao, external_news_dao=external_news_api_dao)

        self.app = create_flask_app(name, self)

    def run(self):
        self.app.run(host="0.0.0.0", debug=self.DEBUG)


def create_web_app():
    return WebApp(name="Thyme", config=Config())
