import pytest
from alembic.command import upgrade as alembic_upgrade  # type: ignore
from alembic.config import Config as AlembicConfig  # type: ignore
from infrastructure.db.connection import DB
from infrastructure.db.daos import DBTasksDAO
from sqlalchemy_utils import (create_database, database_exists,  # type: ignore
                              drop_database)

DATABASE_URL = "postgresql://postgres:pass@postgres:5432/thyme_test"

# pylint: disable=redefined-outer-name


def migrate_db(database_url: str):
    alembic_config = AlembicConfig("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", database_url)
    alembic_upgrade(alembic_config, "head")


@pytest.fixture(scope="session", autouse=True)
def db():
    database_url = DATABASE_URL
    if database_exists(database_url):
        drop_database(database_url)

    create_database(database_url)
    migrate_db(database_url)

    yield DB(url=database_url)

    drop_database(database_url)


@pytest.fixture(scope="function", autouse=True)
def session(db: DB):
    connection = db.engine.connect()
    trans = connection.begin()
    session = db.create_session()

    yield session

    session.close()
    trans.rollback()
    connection.close()


@pytest.fixture(scope="function")
def db_tasks_dao(session):
    yield DBTasksDAO(session=session)
