from aiogram.fsm.state import State, StatesGroup


class Anketa_T (StatesGroup):
    name = State()
    age = State()
    gender = State()