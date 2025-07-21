from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class SearchResult:
    url: str
    title: str = None
    description: str = None


class BaseSearchClient(ABC):
    @abstractmethod
    def search(
        queries: list[str],
        max_count: int) -> list[SearchResult]: pass
