from abc import ABC, abstractmethod
from typing import List

from thyme.news.domain.entities import NewsEntity


class INewsDAO(ABC):
    @abstractmethod
    def get_news(self) -> List[NewsEntity]:
        pass
