from dataclasses import dataclass


@dataclass
class NewsEntity:
    name: str
    content: str


@dataclass
class ExternalNewsEntity:
    id: str
    name: str
    content: str
