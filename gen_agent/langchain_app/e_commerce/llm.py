from langchain.chat_models import init_chat_model
from .settings import ecommerce_setting
import os

os.environ["GROQ_API_KEY"] = ecommerce_setting.GROQ_API_KEY

init_chat_llm=init_chat_model(
    model=ecommerce_setting.MODEL,
    temperature=ecommerce_setting.TEMPERATURE,
    model_provider=ecommerce_setting.MODEL_PROVIDER
)
