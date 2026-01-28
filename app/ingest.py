from pypdf import PdfReader
from app.vectorstore import index, stored_chunks, embedding_model
import numpy as np

def extract_text(file_path: str) -> str:
    """
    Reads text from PDF or TXT files.
    """
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
        return text

    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    else:
        raise ValueError("Unsupported file type")
    

def embed_and_store(chunks: list[str], batch_size: int = 32):
    """
    Converts chunks into embeddings and stores them in FAISS in batches.
    This reduces memory usage for large documents.
    """
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]

        embeddings = embedding_model.encode(batch)
        index.add(np.array(embeddings))
        stored_chunks.extend(batch)
