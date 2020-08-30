from abc import ABC, abstractmethod
from typing import List

from domain.entities import ExternalNewsEntity, NewsEntity


class INewsDAO(ABC):
    @abstractmethod
    def create(self, name: str, content: str) -> NewsEntity:
        pass

    @abstractmethod
    def get_news(self) -> List[NewsEntity]:
        pass


class IExternalNewsDAO(ABC):
    @abstractmethod
    def get_news(self) -> List[ExternalNewsEntity]:
        pass
