# AgentWebSearch Package

## Description

...

## Quickstart

### Create a AgentWebSearch Object

```python
from agentwebsearch import AgentWebSearch
from agentwebsearch.websearch.request import WebSearchRequest

from agentwebsearch.search.client import DefaultSearchClient
from agentwebsearch.llm import OpenAIChatModel
from agentwebsearch.embedding import OpenAIEmbeddingModel


embedding_model = OpenAIEmbeddingModel(
    model="text-embedding-3-large",
    api_key="YOUR_OPENAI_API_KEY"
)

llm = OpenAIChatModel(
    model="gpt-4o-mini",
    api_key="YOUR_OPENAI_API_KEY",
    temperature=0.7
)

search_client = DefaultSearchClient()

websearch = AgentWebSearch(
    search_client=search_client,
    llm=llm,
    embedding_model=embedding_model
)

req = WebSearchRequest(
    ...
)
```
