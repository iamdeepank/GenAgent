from pydantic import BaseModel,Field
from typing import List


class TavilySetting(BaseModel):
    model:str = Field(description="llm model name")
    temperature:float = Field(description="temprature value of model.")

class Source(BaseModel):
    url:str = Field(description="url source.")

class AgentResponse(BaseModel):
    """Schema of Agent Response Answer and source."""
    messages:str=Field(description="answer of agent.")
    source : List[Source] = Field(default_factory=List,description="source of information")
    