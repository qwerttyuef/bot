
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils.executor import start_polling
from config import BOT_TOKEN
from handlers_user import handle_message
from handlers_admin import handle_admin

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.answer("👋 Salom! YouTube yoki Instagram link yuboring.")

@dp.message_handler(lambda m: m.text.startswith('/'))
async def admin_cmd(message: Message):
    await handle_admin(message)

@dp.message_handler()
async def all_msgs(message: Message):
    await handle_message(message)

if __name__ == '__main__':
    start_polling(dp, skip_updates=True)
