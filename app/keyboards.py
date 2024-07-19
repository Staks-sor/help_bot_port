from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Каталог")],
                                     [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакты")]
                                     ], resize_keyboard=True,
                           input_field_placeholder="Выберете пунк меню")

in_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data="catalog")],
    [InlineKeyboardButton(text="Корзина", callback_data=f"basket"), InlineKeyboardButton(text="Контакты", callback_data=f"contacs")]
], resize_keyboard=True,
    input_field_placeholder="Выберете пунк меню")

settings = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="игра", callback_data="list game")]])

game = ["самолет", "танки", "кукуха"]


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for games in game:
        keyboard.add(InlineKeyboardButton(text=games, callback_data=f"games_{games}"))
    return keyboard.adjust(2).as_markup()
