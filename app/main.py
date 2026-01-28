from fastapi import FastAPI, UploadFile, File
from app.ingest import extract_text, embed_and_store
from app.utils import chunk_text
from app.rag import retrieve_chunks
from app.models import QuestionRequest
from app.rag import retrieve_chunks, generate_answer


app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/upload")
def upload_document(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    text = extract_text(file_path)
    chunks = chunk_text(text)

    embed_and_store(chunks)

    return {
        "message": "File uploaded, chunked, and embedded",
        "num_chunks": len(chunks)
    }

@app.post("/ask")
def ask_question(request: QuestionRequest):
    chunks = retrieve_chunks(request.question)

    if not chunks:
        return {"answer": "No relevant information found.", "sources": []}

    answer = generate_answer(chunks, request.question)

    return {
        "answer": answer,
        "sources": chunks
    }