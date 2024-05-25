from peewee import *

db = SqliteDatabase('user_bot.db')

class Student(Model):
    name_s = CharField()
    age_s = CharField()
    gender_s = CharField()
    telegram_id = CharField()
    class Meta:
        database = db
db.connect()
db.create_tables([Student])

