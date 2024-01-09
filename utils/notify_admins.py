import logging

from aiogram import Dispatcher

from data.config import ADMINS
# import sqlite3
# conn = sqlite3.connect('yoqlama.db')
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS group_omon (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     kun TEXT,
#     oy TEXT,
#     keldi TEXT,
#     ketdi TEXT,
# )""")

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            #create database


            await dp.bot.send_message(admin, "Bot ishga tushdi")

        except Exception as err:
            logging.exception(err)
