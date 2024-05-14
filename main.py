import asyncio

from aiogram import Bot, Dispatcher
from handlers import include_routers

bot =Bot(token="7088407944:AAEj6aTi2xMD1BlCan6k8UTSP3cRKFhv2Eo")
db = Dispatcher()


async def main():
    include_routers(db)
    await db.start_polling(bot)
    


if __name__=='___main___':
    asyncio.run(main())
