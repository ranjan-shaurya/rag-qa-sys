import faiss
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Dimension for this model is 384
dimension = 384

# FAISS index (L2 similarity)
index = faiss.IndexFlatL2(dimension)

# Store chunks so we can retrieve text later
stored_chunks = []
