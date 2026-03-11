import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import messages
from langchain_groq import ChatGroq

load_dotenv()

print(os.getenv("TAVILY_API_KEY"))