from tavily import TavilyClient
from langchain.tools import tool

tavily=TavilyClient()

@tool
def tavily_search(query:str): 
    """tavily tool for search."""
    print("user_query", query)
    return tavily.Search(query=query)
