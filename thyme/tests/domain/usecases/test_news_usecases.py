from domain.interfaces import INewsDAO
from domain.usecases.news import GetNewsUseCase


def test_get_all_news_use_case(mock_news_dao: INewsDAO):
    usecase = GetNewsUseCase(news_dao=mock_news_dao)

    news = usecase.execute()

    assert news
