# 🚀 Semantic Search Using Python + Elasticsearch
> using all-mpnet-base-v2 sbert model we create text encoding model for semantic search

> For Install Python Utils

```bash
pip install fastapi uvicorn sentence-transformers pillow

> For Run Project use below commands
```bash
npm run dev

```bash
npm run python

```bash
POST /embed HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json
{
    "sentences":[
        "FastAPI is awesome.",
        "Sentence Transformers make embeddings easy."
    ]
}

> Response
```bash
{
  "sentences": [
    "FastAPI is awesome.",
    "Sentence Transformers make embeddings easy."
  ],
  "embeddings": [
    [0.12, -0.05, ...],   // 768-dim vector
    [0.08, 0.22, ...]     // 768-dim vector
  ]
}