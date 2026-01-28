def chunk_text(text: str, chunk_size=400, overlap=80):
    """
    Splits text into overlapping chunks.
    Chunk size chosen to balance context and retrieval precision.
    """
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start = end - overlap

    return chunks
