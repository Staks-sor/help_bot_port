from aiogram.filters.command import Command, CommandStart

from aiogram.types import Message, CallbackQuery

from Description.Description import greetings_message
from aiogram import F, Router

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"{greetings_message}", reply_markup=kb.in_main)


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


@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer("Вы выбрали каталог игр")
    await callback.message.edit_text('ghbdtn', reply_markup=await kb.inline_cars())
