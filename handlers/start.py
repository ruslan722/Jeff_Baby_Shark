from aiogram import Bot
from aiogram.types import Message


async def get_start(message:Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Привет, я Акуленок Джефф! Я готов к работе \n"
                                               f"Бот помощник по ачивкам в учебных успехах студентов \n"
                                               f"Вы сможете следить за списком своих ачивок \n\n\n")
    