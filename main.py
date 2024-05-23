import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from handlers import include_routers
bot = Bot("7088407944:AAEj6aTi2xMD1BlCan6k8UTSP3cRKFhv2Eo")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Выберите роль:\n"
                          "/student - Зарегистрироваться как студент\n"
                          "/teacher - Зарегистрироваться как преподаватель")




async def main():
    include_routers (dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
