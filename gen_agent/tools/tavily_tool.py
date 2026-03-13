from langchain.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient
load_dotenv()

tavily=TavilyClient()

@tool
def tavily_search(query:str):
    """tavily tool for search."""
    print("user_query", query)
    return tavily.search(query=query)
