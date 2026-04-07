from langchain.messages import HumanMessage, ToolMessage, SystemMessage
from langsmith import traceable
from .tools import get_product_price,apply_discount
from .llm import init_chat_llm


@traceable(name="simple trace test")
def run_agent(query: str):
    tools=[get_product_price,apply_discount]
    llm_call=init_chat_llm.bind_tools(tools)
    print("query:", query)
    response=init_chat_llm.invoke([HumanMessage(content=(query))])
    print("response",response)
    return {"response": "ok"} 


