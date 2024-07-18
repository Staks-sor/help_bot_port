from aiogram.filters.command import Command, CommandStart

from aiogram.types import Message

from Description.Description import greetings_message
from aiogram import F, types, Router

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"{greetings_message}", reply_markup=kb.main)


@router.message(Command("help"))
async def help_function(message: Message):
    await message.answer("я возвращаю help")


@router.message(F.photo)
async def photo_reply(message: Message):
    await message.answer(f"фото: {message.photo[-1].file_id, message.photo[-1].file_size}")
    return f"фото: {message.photo[-1].file_id, message.photo[-1].file_size}"


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAI3O2aY9kFJu8teSjRrCn7UGkQQ2e92AAJH4TEbF9vASDDohaJ1zzGpAQADAgADbQADNQQ")
