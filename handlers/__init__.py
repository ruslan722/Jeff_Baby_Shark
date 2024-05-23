from aiogram import dispatcher

from handlers import user_handlers

def include_routers(dp: dispatcher):
    dp.include_routers(
        user_handlers.router
    )