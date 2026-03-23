from .config import setup_langsmith
from .agents import tavily_agent_call

trace=setup_langsmith()

response=tavily_agent_call()
print(response)



