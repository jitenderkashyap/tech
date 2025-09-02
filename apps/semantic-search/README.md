# 🚀 Semantic Search Using Python + Elasticsearch
all-mpnet-base-v2 sbert model we create text encoding model for semantic search

### Step 1 - Install Python With Modules
```
pip install fastapi uvicorn sentence-transformers pillow
```
### Step 2 - Run Python
```
python sentence_api.py
```
### Step 3 - Create Elastic Index
```
PUT /documents
{
  "mappings": {
    "properties": {
      "text": {
        "type": "text"
      },
      "text_vector": {
        "type": "dense_vector",
        "dims": 768,      // all-mpnet-base-v2 outputs 768-dim vectors
        "index": true,
        "similarity": "cosine"   // or "dot_product" / "l2_norm"
      }
    }
  }
}
```

### Step 4 - Hit Post Request
```
POST 127.0.0.1:8000/embed
Content-Type: application/json
Body:
{
    "sentences":[
        "FastAPI is awesome.",
        "Sentence Transformers make embeddings easy."
    ]
}
```
### Step 5 - Get Response and use embeddings
```
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
```

### Step 6 - Index Document with Embedding
```
POST /documents/_doc/1
{
  "text": "Elasticsearch dense vector search",
  "text_vector": [0.012, -0.043, ..., 0.101]   // embedding array from model
}
```

### Step 7 - KNN Search Query (Dense Vector)
```
POST /documents/_search
{
  "knn": {
    "field": "text_vector",
    "k": 5,
    "num_candidates": 100,
    "query_vector": [0.021, -0.034, ..., 0.178]  // 768-dim normalized vector
  }
}
```
