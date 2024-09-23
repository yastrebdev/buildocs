import asyncio
import logging
import os

from dotenv import load_dotenv
from speech_decoding import speach_recognition

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.handlers import router

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')

bot = Bot(bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')