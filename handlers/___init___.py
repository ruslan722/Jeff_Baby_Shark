from aiogram import Dispatcher

from handlers import anketa, start, rassilka

def include_routers(db: Dispatcher):
    db.include_routers(
        start.router,
        anketa.router
    )

   # db.srartup.register(rassilka.on_startup)