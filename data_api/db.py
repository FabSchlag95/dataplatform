import os
from typing import Generator
from fastapi import HTTPException
from supabase import Client, create_client

from data_api.utils import Embedding


if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL") or ""
SUPABASE_KEY = os.getenv("SUPABASE_API_KEY") or ""

if not all([SUPABASE_KEY, SUPABASE_URL]):
    raise ValueError("Supabase key and value must be not none.")


def get_supabase() -> Generator[Client, None, None]:
    client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    yield client


def save_vectors(embeddings:list[Embedding], table="knowledgebase"):
    client = get_supabase()
    rows = []
    for e in embeddings:
        data = {
            "meta":e.meta,
            "text": e.chunk_text,
            "embedding": e.vector
        }
        rows.append(data)
    res = next(client).table(table).insert(rows).execute()