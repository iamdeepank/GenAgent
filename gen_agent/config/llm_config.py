from langchain_groq import ChatGroq
from gen_agent.settings import llm_settings  

def get_llm():
    return ChatGroq(
        api_key=llm_settings.GROQ_API_KEY,
        model=llm_settings.MODEL,
temperature=llm_settings.TEMPERATURE
)
