from domain.interfaces import INewsDAO


class TestMockNewsDAO:
    def test_get_news(self, mock_news_dao: INewsDAO):
        news = mock_news_dao.get_news()
        assert news
