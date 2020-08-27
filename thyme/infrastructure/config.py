import os


class Config:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    DEBUG = os.environ.get("DEBUG", False)
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
