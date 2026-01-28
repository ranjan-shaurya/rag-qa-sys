import numpy as np
from app.vectorstore import index, stored_chunks, embedding_model

def retrieve_chunks(query: str, top_k: int = 3):
    """
    Embed the query and retrieve top-k similar chunks from FAISS.
    """
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for idx in indices[0]:
        if idx < len(stored_chunks):
            results.append(stored_chunks[idx])

    return results
