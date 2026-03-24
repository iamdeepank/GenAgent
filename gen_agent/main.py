from .config import setup_langsmith
from .agents import tavily_agent_call


setup_langsmith()

from .langchain_app import run_agent
# response=tavily_agent_call()
# print(response)


run_agent("What is the price of laptop?")
