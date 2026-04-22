import json

# Load transcription
with open("transcript.json", "r") as f:
    segments = json.load(f)

chunk_size = 3
chunks = []

for i in range(0, len(segments), chunk_size):

    chunk_text = " ".join(
        [segments[j]["text"] for j in range(i, min(i+chunk_size, len(segments)))]
    )

    chunk_start = segments[i]["start"]
    chunk_end = segments[min(i+chunk_size-1, len(segments)-1)]["end"]

    chunks.append({
        "start": chunk_start,
        "end": chunk_end,
        "text": chunk_text
    })

with open("chunks.json", "w") as f:
    json.dump(chunks, f, indent=2)

print("Chunks saved successfully")

print("\n===== CHUNKS =====\n")

for c in chunks:
    print(c["start"], "-", c["end"])
    print(c["text"])
    print("----------------------")

