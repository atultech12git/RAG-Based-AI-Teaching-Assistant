import whisper
import json

model = whisper.load_model("base")

result = model.transcribe("audio.wav", language="en")

segments = []

for s in result["segments"]:
    segments.append({
        "start": s["start"],
        "end": s["end"],
        "text": s["text"]
    })

with open("transcript.json", "w") as f:
    json.dump(segments, f, indent=2)

print("Transcription completed")

print("\n===== FULL TRANSCRIPTION =====\n")

for s in segments:
    print(f"{s['start']} - {s['end']} : {s['text']}")