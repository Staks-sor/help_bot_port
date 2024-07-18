from aiogram.filters.command import Command, CommandStart

from aiogram.types import Message

from Description.Description import greetings_message
from aiogram import F, types, Router

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"{greetings_message}")
    kb = [
        [
            types.KeyboardButton(text="Регистрация"),
            types.KeyboardButton(text="Без регистрации")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",

    )
    await message.answer("Для полного доступа к системе необходимо зарегистрироваться", reply_markup=keyboard)


@router.message(Command("help"))
async def help_function(message: Message):
    await message.answer("я возвращаю help")


@router.message(F.text == "Регистрация")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")


@router.message(F.text == "Без регистрации")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")


@router.message(F.photo)
async def photo_reply(message: Message):
    await message.answer(f"фото: {message.photo[-1].file_id, message.photo[-1].file_size}")
    return f"фото: {message.photo[-1].file_id, message.photo[-1].file_size}"


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAI3O2aY9kFJu8teSjRrCn7UGkQQ2e92AAJH4TEbF9vASDDohaJ1zzGpAQADAgADbQADNQQ")
