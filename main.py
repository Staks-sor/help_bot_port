import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
import os
from dotenv import load_dotenv
from Description.Description import greetings_message
from aiogram import F

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"{greetings_message}")
    kb = [
        [
            types.KeyboardButton(text="Регистрация[eq[e[qe[eq[eq[eq"),
            types.KeyboardButton(text="Беmmmmm656546540000000000000000000")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",

    )
    await message.answer("vfdgdf", reply_markup=keyboard)


@dp.message(F.text.lower() == "регистрация")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")


@dp.message(F.text.lower() == "без регистрации")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
