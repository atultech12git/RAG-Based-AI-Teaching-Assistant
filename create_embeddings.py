import json
from sentence_transformers import SentenceTransformer

# Load chunks
with open("chunks.json", "r") as f:
    chunks = json.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [c["text"] for c in chunks]

embeddings = model.encode(texts)

print("Embeddings created:", len(embeddings))

print("\n===== EMBEDDINGS =====\n")

for i, emb in enumerate(embeddings):
    print(f"Chunk {i} embedding:")
    print(emb)
    print("----------------------------------")
