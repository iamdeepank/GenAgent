import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

@tool
def brave_search(query: str):
    """Search for weather information."""
    print("User query:", query)
    return "The current weather in Delhi is sunny."

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.1
        )

tools = [brave_search]

agent = create_agent(
    model=llm,
    tools=tools,

)

def main():
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(content="what is the weather in delhi?")
            ]
        }
    )

    print("Result:", result)
    print("content:--",result["messages"][-1].content)

main()