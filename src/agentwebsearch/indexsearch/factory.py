from agentwebsearch.embedding.base import BaseEmbeddingModel
from agentwebsearch.indexsearch.base import BaseInMemoryIndexDB, IndexType
from agentwebsearch.indexsearch.hnsw import HNSWInMemoryIndexDB


class InMemoryIndexDBFactory:
    @staticmethod
    def create(type: IndexType, embedding_model: BaseEmbeddingModel) -> BaseInMemoryIndexDB:
        match type:
            case IndexType.HNSW:
                return HNSWInMemoryIndexDB(embedding_model=embedding_model)
            case _:
                raise ValueError(f"Unsupported indexdb type: {type}")
