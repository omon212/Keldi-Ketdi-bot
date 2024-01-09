from loader import dp

from aiogram import types

import sqlite3


@dp.message_handler(commands='kun')
async def kun(message: types.Message):
    conn = sqlite3.connect('yoqlama.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM group_omon WHERE kun = ? AND oy = ?",
                   (message.date.strftime("%d"), message.date.strftime("%m")))
    result = cursor.fetchall()
    print(result)
    if result == []:
        await message.answer('Bugun yoqlama qilinmagan')
    else:
        await message.answer(f"O`quvchi Omonullo Raimkulov\n\nKeldi: {result[0][3]}\nKetdi: {result[0][4]}")
    # await message.answer(f"O`quvchi Omonullo Raimkulov\n\nKeldi: {result[0][3]}\nKetdi: {result[0][4]}")


@dp.message_handler(commands='7kun')
async def haftalik(message: types.Message):
    import datetime
    x = datetime.datetime.now()
    kun = x.strftime("%d")
    conn = sqlite3.connect('yoqlama.db')
    cursor = conn.cursor()
    hammasi = ''
    for i in range(int(kun) - 6, int(kun) + 1):
        cursor.execute("SELECT * FROM group_omon WHERE kun = ? AND oy = ?", (f'0{i}', x.strftime("%m")))
        a = cursor.fetchall()
        print(a)
        if a == []:
            hammasi += f"Sana {i} Keldi:❌ - Ketdi:❌\n"
        else:
            hammasi += f"Sana {i} - Keldi: {a[0][3]}✅ - Ketdi: {a[0][4]}✅\n"
    await message.answer(hammasi)

@dp.message_handler(commands='1oy')
async def oylik(message:types.Message):
    import datetime
    x = datetime.datetime.now()
    kun = x.strftime("%d")
    conn = sqlite3.connect('yoqlama.db')
    cursor = conn.cursor()
    hammasi = ''
    for i in range(int(kun) - 30, int(kun) + 1):
        cursor.execute("SELECT * FROM group_omon WHERE kun = ? AND oy = ?", (f'0{i}', x.strftime("%m")))
        a = cursor.fetchall()
        print(a)
        if a == []:
            hammasi += f"Sana {i} Keldi:❌ - Ketdi:❌\n"
        else:
            hammasi += f"Sana {i} - Keldi: {a[0][3]}✅ - Ketdi: {a[0][4]}✅\n"
    await message.answer(hammasi)
