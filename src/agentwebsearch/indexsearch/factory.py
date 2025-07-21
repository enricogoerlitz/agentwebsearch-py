from agentwebsearch.embedding.base import BaseEmbeddingModel
from agentwebsearch.indexsearch.base import BaseInMemoryIndexDB, IndexType
from agentwebsearch.indexsearch.hnsw import HNSWInMemoryIndexDB


class InMemoryIndexDBFactory:
    @staticmethod
    def create(type: str, embedding_model: BaseEmbeddingModel) -> BaseInMemoryIndexDB:
        match type:
            case IndexType.HNSW:
                return HNSWInMemoryIndexDB()
            case _:
                raise ValueError(f"Unsupported indexdb type: {type}")
