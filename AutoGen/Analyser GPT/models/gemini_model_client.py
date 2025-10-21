from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL_GEMINI
import os 
from dotenv import load_dotenv
load_dotenv()

from autogen_ext.models.openai import OpenAIChatCompletionClient

open_router_api_key = "your_open_router_api_key_here"  # Replace with your actual OpenRouter API key

def get_model_client():
    open_router_model_client =  OpenAIChatCompletionClient(
    base_url="https://openrouter.ai/api/v1",
    model="tngtech/deepseek-r1t2-chimera:free",
    api_key = open_router_api_key,
    model_info={
        "family":'deepseek',
        "vision" :True,
        "function_calling":True,
        "json_output": False
    }
    )
    return open_router_model_client



