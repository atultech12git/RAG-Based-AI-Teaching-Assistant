from moviepy.editor import VideoFileClip

video = VideoFileClip("video.mp4")

audio = video.audio
audio.write_audiofile("audio.wav")

print("Audio extracted successfully")