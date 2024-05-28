import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from Models import Student, Teacher, Achievements
from keyboard import kb_anketa_cancel_and_back, kb_anketa_cancel, kb_anketa_by_gender
bot = Bot("7088407944:AAEj6aTi2xMD1BlCan6k8UTSP3cRKFhv2Eo")
router = Router()
dp = Dispatcher()
class Anketa_S (StatesGroup):
    achievement = State()
    name_st = State()
    name = State()
    age = State()
    gender = State()
@dp.message(CommandStart())
async def fast_start(message: Message):
    await message.answer(
        text=f"Привет,{message.from_user.full_name}, я акуленок Джефф, я выдаю ачивки студентам, выбери кем зарегистрироваться \n/student\n/teacher",
    )
@dp.message(Command('student'))
async def student(message: Message, state: FSMContext):
    await state.update_data(name_=message.text)
    array_y = []
    for id in Student.select():
        array_y.append(str(id.telegram_id))

    for id in Teacher.select():
        array_y.append(str(id.telegram_id))
    if str(message.from_user.id) in array_y:
        await message.answer(
            text='Вы уже зарегистрированы!',
        )
    else:
        await message.answer(
            text="Введите ваше ФИО:",
            reply_markup=kb_anketa_cancel,
        )
        await state.update_data(name_user=message.text)
        await state.set_state(Anketa_S.name)
@dp.message(Command('teacher'))
async def teacher(message: Message, state: FSMContext):
    await state.update_data(name_user=message.text)
    array_y = []
    for id in Teacher.select():
        array_y.append(str(id.telegram_id))

    for id in Student.select():
        array_y.append(str(id.telegram_id))
    if str(message.from_user.id) in array_y:
        await message.answer(
            text='Вы уже зарегистрированы!',
        )
    else:
        await message.answer(
            text="Введите ваше ФИО:",
            reply_markup=kb_anketa_cancel,
        )
        await state.set_state(Anketa_S.name)
@dp.message(Command('list_student'))
async def list_student(message: Message):
    string_st = ''
    index = 1
    for list_st in Student.select():
        string_st += str(index) + ') ' + list_st.name_s + '\t' + "возраст: " + list_st.age_s + " пол: " + list_st.gender_s + '\n'
        index += 1
    await message.answer(
        text=string_st,
    )
@dp.message(Command('achievements'))
async def achievement(message: Message, state: FSMContext):
    await state.set_state(Anketa_S.achievement)
    array_x = []
    string_n = ''
    index = 0
    for id_s in Student.select():
        array_x.append(str(id_s.telegram_id))
    for ach in Achievements.select():
        index += 1
        string_n += str(index) + ') ' + ach.name + ':\t' + ach.achievements + '\n'
    if str(message.from_user.id) in array_x:
        await message.answer(
            text=f"Список ачивок:\n{string_n}",
        )
    array_y = []
    for id_t in Teacher.select():
        array_y.append(str(id_t.telegram_id))
    if str(message.from_user.id) in array_y:
        await message.answer(
            text=f"Список ачивок:\n{string_n}",
        )
        await message.answer(
            text="Перед тем как присваевать студенту достижение напишите его ФИО:",
        )
@dp.message(Anketa_S.achievement)
async def student_name(message: Message, state: FSMContext):
    await state.update_data(name_st=message.text)
    await message.answer(
        text='Теперь можете написать достижение студента:'
    )
    await state.set_state(Anketa_S.name_st)
@dp.message(Anketa_S.name_st)
async def to_db(message: Message, state: FSMContext):
    user_data = await state.get_data()
    achieve_student = Achievements(name=user_data['name_st'], achievements=message.text)
    achieve_student.save()
    await message.answer(
        text='Все завершилось успешно!',
    )
@dp.message(Anketa_S.name)
async def name_user(message: Message, state: FSMContext):
    await state.update_data(name_=message.text)
    await message.answer(
        text="Введите ваш возраст:",
        reply_markup=kb_anketa_cancel_and_back,
    )
    await state.update_data(tg_id=message.from_user.id)
    await state.set_state(Anketa_S.age)
@dp.message(Anketa_S.age)
async def age_user(message: Message, state: FSMContext):
        try:
            await state.update_data(age_=message.text)
            if int(message.text):
                await message.answer(
                text="Введите свой пол:",
                reply_markup= kb_anketa_by_gender,
                )
            await state.set_state(Anketa_S.gender)
        except:
            await message.answer(
                text="Вы ввели возраст неверно!",
            )
@dp.message(Anketa_S.gender)
async def gender_user(message: Message, state: FSMContext):
    await state.update_data(gender_=message.text)
    if message.text == 'М' or message.text == 'Ж':
        user_data = await state.get_data()
        await message.answer(
            text= f"ФИО: {user_data['name_']}, Возраст: {user_data['age_']}, Пол: {user_data['gender_']}",
        )
        await message.answer(
            text="Регистрация завершена, функционал бота открыт.\n Вы можете просматривать ачивки студентов!",
        )
@dp.callback_query(F.data == 'cancel_anketa')
async def sending(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Регистрация отменена!",
    )
    await state.clear()
@dp.callback_query(Anketa_S.age, F.data == 'back_anketa')
async def go_back_to_name(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Anketa_S.name)
    await callback.message.answer(
    text="Введите ваше ФИО:",
    reply_markup=kb_anketa_cancel,
    )
@dp.callback_query(Anketa_S.gender, F.data == 'back_anketa')
async def go_back_to_name(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Anketa_S.age)
    await callback.message.answer(
    text="Введите ваш возраст:",
    reply_markup=kb_anketa_cancel_and_back,
    )
@dp.callback_query(Anketa_S.gender, F.data.startswith('gender_'))
async def gender_choice(callback: CallbackQuery, state: FSMContext):
    gender = 'М' if callback.data == 'gender_m' else 'Ж'
    await state.update_data(gender_=gender)
    user_data = await state.get_data()
    name = user_data.get('name_')
    age = user_data.get('age_')
    gender = user_data.get('gender_')
    tg_id = user_data.get('tg_id')
    user_bot = user_data.get('name_user')
    if user_bot == '/student':
        await callback.message.answer(
            text=f"Имя: {name}, Возраст: {age}, Пол: {gender}\nРегистрация завершена. Функционал бота открыт. Вы можете просматривать ачивки студентов!",
        )
        user_student = Student(name_s=name, age_s=age, gender_s=gender, telegram_id=tg_id)
        user_student.save()
    else:
        await callback.message.answer(
            text=f"ФИО: {name}, Возраст: {age}, Пол: {gender}\nРегистрация завершена. Доступ к функциям бота открыт.\nВы можете просматривать количество зарегистрированных студентов и выдавать ачивки использовав команду:\n/achievements",
        )
        user_teacher = Teacher(name_s=name, age_s=age, gender_s=gender, telegram_id=tg_id)
        user_teacher.save()
    await state.clear()


async def main():
    logging.basicConfig(level=logging.INFO)
 
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Succes!!!")