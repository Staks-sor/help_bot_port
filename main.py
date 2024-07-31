import asyncio
import logging
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

from app.hendlers import router
from fsm import router as fsm_router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Включаем логирование, чтобы не пропустить важные сообщения

# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

dp.include_router(router)
dp.include_router(fsm_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
