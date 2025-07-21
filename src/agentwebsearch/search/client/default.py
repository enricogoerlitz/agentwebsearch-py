import googlesearch

from typing import Iterator
from urllib.parse import urlparse

from agentwebsearch.search.client.base import (
    BaseSearchClient, SearchResult
)


class DefaultSearchClient(BaseSearchClient):
    def search(self, queries: list[str], n: int) -> list[SearchResult]:
        search_links = [
            SearchResult(url=link) for i, query in enumerate(queries)
            for link in self._search(query, n, i)
            if self._filter_condition(link)
        ]

        max_link_count = len(queries) * n
        self._unique_links(search_links, max_link_count)

        return search_links

    def _search(self, query: str, n: int, i: int) -> Iterator[str]:
        yield from googlesearch.search(
            term=query.strip(),
            num_results=self._n_results(n, i)
        )

    def _unique_links(self, results: list[SearchResult], max_link_count: int) -> list[str]:
        seen = set()
        search_links = [
            result
            for result in results
            if not (
                urlparse(result.url).path in seen or
                seen.add(urlparse(result.url).path)
            )
        ][:max_link_count]

        return search_links

    def _filter_condition(self, link: str) -> bool:
        return (
            link.startswith("http") and
            not link.startswith("https://www.google.com/search?") and
            ".pdf" not in link
        )

    def _n_results(self, n: int, i: int) -> int:
        max_num = int(n * 2)
        num = int(n + (n * i) / 3)
        return num if num < max_num else max_num
