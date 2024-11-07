import os
from dotenv import load_dotenv
import google.generativeai as genai
import nest_asyncio
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI

class SQLAgentConfig:
    def __init__(self):
        self._setup_async()
        self._load_environment()
        self._configure_genai()

    def _setup_async(self):
        nest_asyncio.apply()
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

    def _load_environment(self):
        load_dotenv()
        if 'GOOGLE_API_KEY' not in os.environ:
            raise ValueError("请确保设置了 GOOGLE_API_KEY 环境变量")

    def _configure_genai(self):
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

    def create_model(self):
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest") 