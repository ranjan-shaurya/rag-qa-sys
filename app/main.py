from fastapi import FastAPI, UploadFile, File
from app.ingest import extract_text
from app.utils import chunk_text

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

    return {
        "message": "File uploaded and processed",
        "num_chunks": len(chunks)
    }
