import responses
from domain.entities import NewsEntity
from domain.interfaces import IExternalNewsDAO, INewsDAO
from domain.usecases.news import GetNewsUseCase, ImportNewsUseCase


def test_get_all_news_use_case(mock_news_dao: INewsDAO):
    name = "name"
    content = "content"
    mock_news_dao.create(name=name, content=content)

    usecase = GetNewsUseCase(news_dao=mock_news_dao)

    news = usecase.execute()

    assert news


@responses.activate
def test_import_news_use_case(mock_news_dao: INewsDAO, external_news_dao: IExternalNewsDAO):
    usecase = ImportNewsUseCase(news_dao=mock_news_dao, external_news_dao=external_news_dao)

    json = {
        "articles": [
            {
                "url": "test_utl.com",
                "title": "test_title",
                "description": "test_description",
            }
        ],
    }
    responses.add(responses.GET, f"https://newsapi.org/v2/top-headlines", json=json, status=200, match_querystring=False)

    usecase.execute()

    assert mock_news_dao.get_news()[0] == NewsEntity(name="test_title", content="test_description")
    assert responses.calls[0].request.params == {"language": "ru", "apiKey": "test"}
