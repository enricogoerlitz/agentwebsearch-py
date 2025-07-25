from fastmcp import FastMCP

from agentwebsearch import AgentWebSearch


class WebSearchFastMCP(FastMCP):
    def __init__(
            self,
            websearch: AgentWebSearch,
            **fastmcp_kwargs
    ):
        super().__init__(**fastmcp_kwargs)
        self._websearch = websearch
        self.tool(self.websearch)

    def websearch(self, query: str) -> str:
        """Search the web for a given query and return results."""
        # Placeholder for actual web search logic
        return f"Results for '{query}'"
