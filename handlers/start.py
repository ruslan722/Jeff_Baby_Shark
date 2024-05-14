from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
from keyboards.start import *
from main import bot

router = Router()

@router.message(Command("start"))
async def start_hander(msg: Message):

    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='anketa', description='Справка'),
        BotCommand(command='get_achievement', description='Получить ачивку'),
    ])

    await msg.answer(text="Получение ачивок", reply_markup=kb_start_next)

@router.callback_query(F.data =='next')
async def next_handrer(callback_query: CallbackQuery):

    await callback_query.message.edit_text(
        'Страница 2', reply_markup=kb_start_back)

@router.callback_query(F.data == 'back')
async def back_handler(callback_query: CallbackQuery):
    await callback_query.message.delete()
    

