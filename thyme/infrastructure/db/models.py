from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NewsORM(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(Text)

    def __repr__(self):
        return f"<News(id={self.id}, name='{self.name}', content='{self.content}')>"
