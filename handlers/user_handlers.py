from aiogram import  Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils. Anketa_student import Anketa_S
from utils.Anketa_teacher import Anketa_T
from keyboards.user_keyboards import *

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Выберите роль:\n"
                          "/student - Зарегистрироваться как студент\n"
                          "/teacher - Зарегистрироваться как преподаватель")

@router.message(Command("student"))
async def register_student_handler(message: Message, state: FSMContext):
    await state.set_state(Anketa_S.name)
    await message.answer('Скажите свое имя', reply_markup=kb_anketa_cancel)

@router.callback_query(F.data == 'cancel_anketa')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer('Регистрация была отменена, захочешь заплывай в мой океан')

@router.message(Anketa_S.name)
async def student_name_by_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Anketa_S.age)
    await message.answer(
        'Скажи свой возраст',

@router.message(Command("teacher"))
async def register_teacher_handler(message: Message):
  
