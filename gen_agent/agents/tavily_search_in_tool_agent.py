import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from gen_agent.tools import tavily_search
from gen_agent.config import llm

tools=[tavily_search]






