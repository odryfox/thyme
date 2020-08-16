import sqlalchemy
from sqlalchemy import orm


def create_session(url: str):
    engine = sqlalchemy.create_engine(url)
    session = orm.scoped_session(orm.sessionmaker(bind=engine))
    return session
