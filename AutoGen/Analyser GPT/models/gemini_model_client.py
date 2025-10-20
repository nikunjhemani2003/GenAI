from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL_GEMINI
from dotenv import load_dotenv
load_dotenv()
import os 

from autogen_ext.models.openai import OpenAIChatCompletionClient

open_router_api_key = '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'

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



