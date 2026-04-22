import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# load chunks
with open("chunks.json", "r") as f:
    chunks = json.load(f)

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# extract text from chunks
texts = [c["text"] for c in chunks]

# create embeddings
embeddings = model.encode(texts)

# create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# add embeddings
index.add(np.array(embeddings))

# save index
faiss.write_index(index, "video_index.faiss")

print("Vector database saved")