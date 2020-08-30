from typing import Dict, List

import requests
from domain.entities import ExternalNewsEntity
from domain.interfaces import IExternalNewsDAO


class ExternalNewsAPIDAO(IExternalNewsDAO):
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.language = "ru"
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def _get_raw_news(self) -> List[Dict]:
        params = {
            "language": self.language,
            "apiKey": self.api_key,
        }
        response = requests.get(self.base_url, params=params)
        json_response = response.json()
        return json_response["articles"]

    def _raw_news_to_news_entity(self, raw_news: Dict) -> ExternalNewsEntity:
        return ExternalNewsEntity(
            id=raw_news["url"],
            name=raw_news["title"],
            content=raw_news["description"],
        )

    def get_news(self) -> List[ExternalNewsEntity]:
        raw_news = self._get_raw_news()
        news_entities = [self._raw_news_to_news_entity(n) for n in raw_news]
        return news_entities
