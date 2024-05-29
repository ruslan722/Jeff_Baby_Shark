from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
kb_anketa_cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa')
        ]])

kb_anketa_cancel_and_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(
            text='Назад',
            callback_data='back_anketa'),
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa'),]]
        )
kb_anketa_by_gender = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Мужской',
            callback_data='gender_m',
        ),
        InlineKeyboardButton(
            text='Женский',
            callback_data= 'gender_w',),
    ],[
        InlineKeyboardButton(
            text='Назад',
            callback_data='back_anketa'),
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa'),
    ]])
def key_user():
    button_teacher = KeyboardButton(text='Учитель')
    button_student = KeyboardButton(text='Студент')
    button_list = KeyboardButton(text='Лист студентов')
    button_achivments = KeyboardButton(text='Ачивки')
    button_1 = [button_student]
    button_2 = [button_teacher]
    button_3 = [button_list]
    button_4 = [button_achivments]
    markup = ReplyKeyboardMarkup(
        keyboard=[button_1, button_2, button_3, button_4],
        resize_keyboard=True,
    )
    return markup