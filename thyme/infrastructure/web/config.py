import os


class Config:
    DATABASE_URL: str = os.environ["DATABASE_URL"]
    DEBUG: bool = os.environ.get("DEBUG", "False") == "True"
