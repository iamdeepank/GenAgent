from langchain.agents import create_agent
from gen_agent.tools import brave_search
from gen_agent.config import llm
from langchain.messages import HumanMessage
from gen_agent.settings import AgentResponse

tools=[brave_search]

agent=create_agent(model=llm,tools=tools,response_format=AgentResponse)

def tavily_agent_call():
    content=agent.invoke(
        {
            "messages": [HumanMessage(content="who is Ambani?")]
        }
    )
    return content

