
from aiogram import types
from config import ADMINS
from database import count_users, get_top_download

FORCE_SUB = False
CHANNEL_USERNAME = None

def is_admin(user_id):
    return user_id in ADMINS

async def handle_admin(message: types.Message):
    global FORCE_SUB, CHANNEL_USERNAME
    user_id = message.from_user.id
    if not is_admin(user_id): return

    text = message.text.strip()

    if text.startswith('/kanal'):
        if 'off' in text:
            FORCE_SUB = False
            CHANNEL_USERNAME = None
            await message.answer("Majburiy kanal o‘chirildi.")
        else:
            parts = text.split()
            if len(parts) >= 2:
                CHANNEL_USERNAME = parts[1]
                FORCE_SUB = True
                await message.answer(f"Kanal sozlandi: {CHANNEL_USERNAME}")
    elif text == '/stat':
        insta = get_top_download('instagram') or ('-', 0)
        yt = get_top_download('youtube') or ('-', 0)
        users = count_users()
        await message.answer(
            f"👤 Foydalanuvchilar: {users}\n"
            f"📸 Instagram top: {insta[0]} ({insta[1]} marta)\n"
            f"▶️ YouTube top: {yt[0]} ({yt[1]} marta)"
        )
    elif text.startswith('/rek'):
        await message.answer("📢 Reklama xabarini rasm va matn bilan yuboring.")
