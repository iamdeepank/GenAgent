from langchain.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient
load_dotenv()

tavily=TavilyClient()

@tool
def brave_search(query:str):
    """tavily tool for search."""
    return tavily.search(query=query)
