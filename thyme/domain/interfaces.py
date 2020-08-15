from abc import ABC, abstractmethod
from typing import List

from domain.entities import NewsEntity


class INewsDAO(ABC):
    @abstractmethod
    def get_news(self) -> List[NewsEntity]:
        pass
