from agentwebsearch.search.client.base import (
    BaseSearchClient,
    SearchResult,
)


class SearchApiClient(BaseSearchClient):
    def search(self, queries: list[str], n: int) -> list[SearchResult]:
        raise NotImplementedError("SearchApiClient is not implemented yet.")
