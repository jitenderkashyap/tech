from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import uvicorn
from typing import List

# pip install fastapi uvicorn sentence-transformers pillow

# Load the sentence transformer model
model = SentenceTransformer('all-mpnet-base-v2')

# Create FastAPI app
app = FastAPI()

# Request body model
class SentenceRequest(BaseModel):
    sentences: List[str]

# API endpoint
@app.post("/embed")
def get_embedding(request: SentenceRequest):
    embeddings = model.encode(request.sentences)
    return {
        "sentences": request.sentences,
        "embeddings": [emb.tolist() for emb in embeddings]
    }

if __name__ == "__main__":
    uvicorn.run("sentence_api:app", host="127.0.0.1", port=8000, reload=True)
