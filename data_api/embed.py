from typing import List
from langchain_openai import ChatOpenAI
from openai import OpenAI, api_key
import os
from dotenv import load_dotenv
load_dotenv()
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL") or ""
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or ""

KEY = os.getenv("OPENAI_API_KEY") or ""
client = OpenAI(api_key=KEY)


def embed(texts: List[str]):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )
    return [d.embedding for d in response.data]
