import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


# convert seconds to minutes:seconds
def format_time(seconds):
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"


# load chunks
with open("chunks.json", "r") as f:
    chunks = json.load(f)


# load vector index
index = faiss.read_index("video_index.faiss")


# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# ask user query
query = input("Ask your question: ")


# convert query to embedding
query_embedding = model.encode([query])


# search vector database
D, I = index.search(np.array(query_embedding), k=3)


print("\n===== SEARCH RESULTS =====\n")


for idx in I[0]:

    c = chunks[idx]

    start_time = format_time(c["start"])
    end_time = format_time(c["end"])

    print("Time:", start_time, "-", end_time)
    print("Text:", c["text"])
    print("----------------------------------")