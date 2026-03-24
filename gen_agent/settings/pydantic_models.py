from pydantic import BaseModel,Field
from typing import List,Optional

class Source(BaseModel):
    url:str = Field(description="url source.")
    title: Optional[str] = Field(default=None, description="Page title")
    content_snippet: Optional[str] = Field(default=None, description="Extracted snippet")
    score: Optional[float] = Field(default=None, description="Relevance score")
    source_type: Optional[str] = Field(default="web", description="Type of source")

class AgentResponse(BaseModel):
    """Schema of Agent Response Answer and source."""
    messages:str=Field(description="answer of agent.")
    source : List[Source] = Field(default_factory=List,description="source of information")
    