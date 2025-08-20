from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from ibm_watsonx_orchestrate.run import connections
from tavily import TavilyClient

@tool(name="web_search", description="Search the web.", permission=ToolPermission.READ_ONLY)
def web_search(query: str) -> dict:
    """
    Search the web for relevant information using Tavily Search.

    Args:
        query (str): The search query string.
        url (str): the url where search results must come from

    Returns:
        dict: A dictionary of search results obtained from Tavily search.
    """
    try:
        conn = connections.api_key_auth('tavily')
        tavily_client = TavilyClient(api_key=conn.api_key)
        response = tavily_client.search(query=query, max_results=5, include_answer=True)
        return response
    except Exception as e:
       return (f"Unexpected Error: {e}")