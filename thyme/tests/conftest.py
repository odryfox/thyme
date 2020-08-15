import pytest

from infrastructure.db.daos import MockNewsDAO


@pytest.fixture(scope='session')
def mock_news_dao():
    return MockNewsDAO()
