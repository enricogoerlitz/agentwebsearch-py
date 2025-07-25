# AgentWebSearch Package
[![CI](https://github.com/enricogoerlitz/agentwebsearch-py/actions/workflows/ci.yml/badge.svg)](https://github.com/enricogoerlitz/agentwebsearch-py/actions/workflows/ci.yml)
[![CD](https://github.com/enricogoerlitz/agentwebsearch-py/actions/workflows/release.yml/badge.svg)](https://github.com/enricogoerlitz/agentwebsearch-py/actions/workflows/release.yml)

## Description

**AgentWebSearch** is a modular Python package designed to perform web searches and extract only semantically relevant information for efficient use in LLM contexts (e.g. RAG pipelines or autonomous agents).

It combines keyword-based and vector-based search strategies to return concise, high-relevance results while minimizing token overhead. A given input (e.g. a user query or message history) is processed via an LLM to extract one or more search questions. These are then used to perform both:

- **Web search** (via Google Search or pluggable APIs like SerpAPI or SearchAPI)
- **Vector search** (on a temporary in-memory HNSW index using `hnswlib`)

Fetched pages are scraped (via `requests`), chunked, embedded, and stored in an in-memory vector index. This allows for efficient semantic filtering of irrelevant content before assembling the final result set.

The package supports full customization:
- Replace or extend components like `SearchClient`, `WebScraper`, or `EmbeddingModel`
- Plug in your own LLM or embedding backends
- Deploy via **REST API** (FastAPI) or as a **Modular Command Protocol (MCP)** agent

Use cases include tools for LLM agents, chat systems with real-time web context, or any pipeline that benefits from semantically filtered live search results.

## Quickstart

### Create a AgentWebSearch Object

```python
from agentwebsearch import AgentWebSearch
from agentwebsearch.websearch.request import WebSearchRequest
from agentwebsearch.search.client import DefaultSearchClient
from agentwebsearch.webscraper import DefaultWebScraper
from agentwebsearch.indexsearch import HNSWInMemoryIndexDB
from agentwebsearch.llm import OpenAIChatModel
from agentwebsearch.embedding import OpenAIEmbeddingModel


embedding_model = OpenAIEmbeddingModel(
    model="text-embedding-3-large",
    api_key="YOUR_OPENAI_API_KEY"
)

llm = OpenAIChatModel(
    model="gpt-4o",
    api_key="YOUR_OPENAI_API_KEY",
    temperature=0.7
)

index_db = HNSWInMemoryIndexDB(embedding_model=embedding_model)
search_client = DefaultSearchClient()
scraper = DefaultWebScraper()

websearch = AgentWebSearch(
    search_client=search_client,
    index_db=index_db,
    scraper=scraper,
    llm=llm,
    embedding_model=embedding_model
)
```

### Execute AgentWebSearch

```python
from agentwebsearch.websearch.request import RequestQuery, RequestQueryMessage

req = WebSearchRequest(
    query=RequestQuery(
        messages=[
            RequestQueryMessage(
                role="user",
                content="Wann wurde der Bundeskanzler 2025 gewählt?"
            )
        ]
    )
)

result = websearch.execute(req)
# or
for result in websearch.execute(req, stream=True):
    print(result)
    yield result
```

### Deploy as MCP-Server

```python
# server.py
from agentwebsearch import AgentWebSearch
from agentwebsearch.mcp import WebSearchFastMCP


websearch = AgentWebSearch(...)
mcp = WebSearchFastMCP(
    websearch=websearch,
    name="Demo 🚀"
)


@mcp.tool
def other_tool():
    return "Other tool"


if __name__ == "__main__":
    # available tools:
    #   - websearch
    #   - other_tool

    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8000,
        path="/mcp"
    )

# python run server.py
```

### Deploy as REST-API


```python
# server.py
from agentwebsearch import AgentWebSearch
from agentwebsearch.rest import WebSearchFastAPI

websearch = AgentWebSearch(...)
app = WebSearchFastAPI(
    websearch=websearch,
    name="Demo 🚀"
)

@app.get("/other-route")
def other_route():
    return {"message": "Other route"}


# uvicorn agentwebsearch.rest.example:app --reload --app-dir src
```
