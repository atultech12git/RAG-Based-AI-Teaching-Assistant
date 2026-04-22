import yt_dlp

url = input("Enter YouTube video URL: ")

ydl_opts = {
    'format': 'mp4',
    'outtmpl': 'video.mp4'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully")