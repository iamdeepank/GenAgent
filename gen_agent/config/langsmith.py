import os
from gen_agent.settings import langsmith_settings

def setup_langsmith():
    if langsmith_settings.LANGSMITH_TRACING:
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_ENDPOINT"] = langsmith_settings.LANGSMITH_ENDPOINT
        os.environ["LANGCHAIN_API_KEY"] = langsmith_settings.LANGSMITH_API_KEY
        os.environ["LANGCHAIN_PROJECT"] = langsmith_settings.LANGSMITH_PROJECT
    
    return "done"    
