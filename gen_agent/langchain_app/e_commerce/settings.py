from pydantic_settings import BaseSettings
from pydantic import Field


class EcommerceAppSettings(BaseSettings):
    """Settings for ecom application."""
    MAX_ITERATIONS:int = Field(default=10,description="number of times tool call.")
    MODEL:str = Field(default="llama-3.1-8b-instant",description="name of the model.")
    TEMPERATURE:float = Field(default=0.1,description="model temperature.")

ecommerce_setting=EcommerceAppSettings()    


