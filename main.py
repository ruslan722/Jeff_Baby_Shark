import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from utils.commands import set_commands
from handlers.start import get_start
from aiogram.filters import Command
load_dotenv('.env')

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot =Bot(token=token)
dp =Dispatcher()

async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='Привет! Я Акуленок Джефф, я готов к работе.')

    dp.startup.register(start_bot)

dp.message.register(get_start, Command(commands='start'))


async def main():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
