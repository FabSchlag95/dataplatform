from db import get_supabase
from embed import embed
import numpy as np


def search_similar(query, table="knowledgebase"):

    client = get_supabase()

    if not query:
        raise Exception("Empty query.")
    
    query_vector = embed([query])[0]

    sql = f""" * ORDER BY embedding <-> '{query_vector}' LIMIT 5;"""

    res = next(client).table(table).select(sql).execute()
    return res.data

def search_similar_2(query, table="knowledgebase"):
    client = get_supabase()
    chunks = next(client).table(table).select("*").execute().data

    ranked_embeddings = []
    query_vector = embed([query])[0]
    
    for e in chunks:
        array_ = eval(e["embedding"])
        similarity = np.array(array_,dtype="float32") @ np.array(query_vector)
        ranked_embeddings.append((similarity, e))
    ranked_embeddings.sort(key=lambda x:x[0], reverse=True)

    return ranked_embeddings[:5]