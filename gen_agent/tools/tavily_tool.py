from langchain.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient
from gen_agent.settings import tavily_settings  

tavily=TavilyClient(api_key=tavily_settings.API_KEY)

@tool
def brave_search(query:str):
    """tavily tool for search."""
    return tavily.search(query=query)
