
from aiogram import types
from database import add_user, add_download
from utils import download_youtube, download_instagram
import os

async def handle_message(message: types.Message):
    user_id = message.from_user.id
    add_user(user_id)
    text = message.text.strip()

    if 'youtube.com' in text or 'youtu.be' in text:
        path = download_youtube(text)
        add_download(text, 'youtube')
        await message.answer_video(open(path, 'rb'))
        os.remove(path)
    elif 'instagram.com' in text:
        path = download_instagram(text)
        add_download(text, 'instagram')
        await message.answer_video(open(path, 'rb'))
        os.remove(path)
    else:
        await message.answer("Video havolasini yuboring (YouTube yoki Instagram)")
