from dotenv import load_dotenv
from langchain.agents import create_agent
from gen_agent.tools import tavily_search
from gen_agent.config import llm
from langchain.messages import HumanMessage
load_dotenv()

tools=[tavily_search]

agent=create_agent(model=llm,tools=tools)

content=agent.invoke(
     {
        "messages": [HumanMessage(content="who is Ambani?")]
    }
)
print("contenttt",content)

