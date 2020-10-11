import os


class Config:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    DEBUG = os.environ.get("DEBUG", False)
