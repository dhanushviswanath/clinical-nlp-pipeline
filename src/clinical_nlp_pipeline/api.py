from fastapi import FastAPI
from pydantic import BaseModel

from .pipeline import run_pipeline

app = FastAPI(title="Clinical NLP Pipeline")

class NoteRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process")
def process_note(payload: NoteRequest):
    return run_pipeline(payload.text)
