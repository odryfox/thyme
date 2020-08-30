from typing import List

from domain.entities import NewsEntity
from domain.interfaces import IExternalNewsDAO, INewsDAO


class GetNewsUseCase:
    def __init__(self, news_dao: INewsDAO):
        self.news_dao = news_dao

    def execute(self) -> List[NewsEntity]:
        news = self.news_dao.get_news()
        return news


class ImportNewsUseCase:
    def __init__(self, news_dao: INewsDAO, external_news_dao: IExternalNewsDAO):
        self.news_dao = news_dao
        self.external_news_dao = external_news_dao

    def execute(self) -> None:
        external_news_entities = self.external_news_dao.get_news()

        for external_news_entity in external_news_entities:
            self.news_dao.create(name=external_news_entity.name, content=external_news_entity.content)
