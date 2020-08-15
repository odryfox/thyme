from typing import List

from domain.entities import NewsEntity
from domain.interfaces import INewsDAO


class MockNewsDAO(INewsDAO):
    def get_news(self) -> List[NewsEntity]:
        news = [NewsEntity(name='name', content='content')]
        return news
