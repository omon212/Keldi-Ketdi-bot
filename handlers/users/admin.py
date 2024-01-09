from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.keldi_ketdi import keldi_button, ketdi_button
from aiogram.types import Message
from loader import AdminClasses


@dp.message_handler(commands='admin')
async def adminka(message: Message):
    conn = sqlite3.connect('yoqlama.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS group_omon (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kun TEXT,
        oy TEXT,
        keldi TEXT,
        ketdi TEXT
    )""")
    if message.from_user.id == 6498877955:
        await message.answer('Admin panelga xush kelibsiz', reply_markup=keldi_button)
        await AdminClasses.login_admin.set()


import datetime
import sqlite3


@dp.message_handler(state=AdminClasses.login_admin, text='Keldi')
async def login_admin(message: Message, state: FSMContext):
    conn = sqlite3.connect('yoqlama.db')
    cursor = conn.cursor()
    # cursor.execute("INSERT INTO group_omon VALUES (NULL, ?, ?, ?, ?)", (
    #     datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%m"),
    #     datetime.datetime.now().strftime("%X"), None))
    # conn.commit()

    # Check if there is data for the current day
    cursor.execute("SELECT * FROM group_omon WHERE kun = ? AND oy = ?", (
        datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%m")))
    result = cursor.fetchall()
    print(result)
    a = []
    if result != a:

        await message.answer('Bugungi yoqlama qilib bo`lingan')
    else:
        await message.answer('Keldi', reply_markup=ketdi_button)
        print('else')
        cursor.execute("INSERT INTO group_omon VALUES (NULL, ?, ?, ?, ?)", (
            datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%m"),
            datetime.datetime.now().strftime("%X"), None))
        conn.commit()


        # If there is no data, print a message





@dp.message_handler(state=AdminClasses.login_admin, text='Ketdi')
async def ketdi_admin(message: Message):
    conn = sqlite3.connect('yoqlama.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE group_omon SET ketdi = ? WHERE ketdi IS NULL", (datetime.datetime.now().strftime("%X"),))
    conn.commit()
    await message.answer('Ketdi', reply_markup=keldi_button)
