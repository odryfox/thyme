from domain.interfaces import INewsDAO
from infrastructure.db.daos import DBNewsDAO


class TestMockNewsDAO:
    def test_get_news(self, mock_news_dao: INewsDAO):
        name = "name"
        content = "content"

        mock_news_dao.create(name=name, content=content)

        news = mock_news_dao.get_news()

        assert len(news) == 1
        assert news[0].name == name
        assert news[0].content == content


class TestDBNewsDAO:
    def test_get_news(self, db_news_dao: DBNewsDAO):
        name = "name"
        content = "content"

        db_news_dao.create(name=name, content=content)

        news = db_news_dao.get_news()

        assert len(news) == 1
        assert news[0].name == name
        assert news[0].content == content
