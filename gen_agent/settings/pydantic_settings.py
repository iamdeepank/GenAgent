from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class LLMSettings(BaseSettings):
    GROQ_API_KEY:str= Field(description="Groq api key.")
    MODEL:str = Field(description="llm model name")
    TEMPERATURE:float = Field(description="temprature value of model.")

    class Config:
        env_prefix = "LLM_"

class TavilySettings(BaseSettings):
    API_KEY:str = Field(description="tavily api key.")

    class Config:
        env_prefix = "TAVILY_"

class LangSmithSettings(BaseSettings):
    LANGSMITH_TRACING: bool = Field(default=False)
    LANGSMITH_ENDPOINT: Optional[str] = Field(default=None)
    LANGSMITH_API_KEY: Optional[str] = Field(default=None)
    LANGSMITH_PROJECT: Optional[str] = Field(default=None)

    class Config:
        env_prefix = ""


llm_settings=LLMSettings() 
tavily_settings=TavilySettings()
langsmith_settings=LangSmithSettings()       