from typing import List

from thyme.news.domain.entities import NewsEntity
from thyme.news.domain.interfaces import INewsDAO


class MockNewsDAO(INewsDAO):
    def get_news(self) -> List[NewsEntity]:
        news = [NewsEntity(name='name', content='content')]
        return news
