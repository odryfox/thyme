from typing import List

from sqlalchemy.orm import Session

from domain.entities import NewsEntity
from domain.interfaces import INewsDAO
from infrastructure.db.models import NewsORM


class MockNewsDAO(INewsDAO):
    def get_news(self) -> List[NewsEntity]:
        news = [NewsEntity(name='name', content='content')]
        return news


class DBNewsDAO(INewsDAO):
    def __init__(self, session: Session):
        self.session = session

    def _news_orm_to_news_entity(self, news_orm: NewsORM):
        return NewsEntity(
            name=news_orm.name,
            content=news_orm.content,
        )

    def create(self, name: str, content: str) -> NewsEntity:
        news_orm = NewsORM(name=name, content=content)
        self.session.add(news_orm)
        self.session.commit()
        news_entity = self._news_orm_to_news_entity(news_orm)
        return news_entity

    def get_news(self) -> List[NewsEntity]:
        news_orm = self.session.query(NewsORM).all()
        news_entities = [self._news_orm_to_news_entity(n) for n in news_orm]
        return news_entities
