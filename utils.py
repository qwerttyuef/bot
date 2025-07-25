
import yt_dlp
import os
import uuid

def download_video(url, platform):
    os.makedirs("downloads", exist_ok=True)
    temp_id = str(uuid.uuid4())
    output_path = f"downloads/{platform}_{temp_id}.mp4"

    ydl_opts = {
        'outtmpl': output_path,
        'format': 'mp4',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_path

def download_youtube(url):
    return download_video(url, 'youtube')

def download_instagram(url):
    return download_video(url, 'instagram')
