import yt_dlp

url = input("Enter Link: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])


print("Video downloaded succesfully Tyrrick")