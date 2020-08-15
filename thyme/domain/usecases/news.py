from typing import List

from domain.entities import NewsEntity
from domain.interfaces import INewsDAO


class GetNewsUseCase:
    def __init__(self, news_dao: INewsDAO):
        self.news_dao = news_dao

    def execute(self) -> List[NewsEntity]:
        news = self.news_dao.get_news()
        return news
