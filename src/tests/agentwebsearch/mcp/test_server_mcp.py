from agentwebsearch.mcp.server import WebSearchFastMCP


def test_fastmcp_has_websearch():
    mcp = WebSearchFastMCP(websearch=None, name="test-mcp")
    assert mcp.name == "test-mcp"
    assert hasattr(mcp, "websearch")
    assert callable(mcp.websearch)
