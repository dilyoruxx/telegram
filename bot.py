import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from config import token

bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command('start', 'hi'))
async def start(message:Message):
    await message.answer("Привет, как дела ?")
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())