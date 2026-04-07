from .config import setup_langsmith
from .agents import tavily_agent_call
from .langchain_app import run_agent


setup_langsmith()

## Tavily Agent
# response=tavily_agent_call()
# print(response)


run_agent("What is the price of laptop?")
