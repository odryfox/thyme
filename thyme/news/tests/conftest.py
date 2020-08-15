import pytest

from thyme.news.infrastructure.daos.news_dao import MockNewsDAO


@pytest.fixture(scope='session')
def mock_news_dao():
    return MockNewsDAO()
