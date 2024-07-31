from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


# Определяем состояния
class Registration(StatesGroup):
    waiting_for_tab_number = State()
    waiting_for_full_name = State()


# Начало регистрации
@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await message.answer("Введите ваш табельный номер:")
    await state.set_state(Registration.waiting_for_tab_number)


# Получение табельного номера
@router.message(Registration.waiting_for_tab_number)
async def process_tab_number(message: Message, state: FSMContext):
    await state.update_data(tab_number=message.text)
    await message.answer("Введите ваше ФИО:")
    await state.set_state(Registration.waiting_for_full_name)


# Получение ФИО
@router.message(Registration.waiting_for_full_name)
async def process_full_name(message: Message, state: FSMContext):
    user_data = await state.get_data()
    tab_number = user_data['tab_number']
    full_name = message.text

    await message.answer(f"Регистрация завершена!\nТабельный номер: {tab_number}\nФИО: {full_name}")
    await state.clear()  # Сброс состояния
