from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Aleykkum, {message.from_user.full_name}!\n\nBot komandalari:\n\n/kun - Bugungi kun ma`lumotlarini ko`rish\n/7kun - 1 haftalik ma`lumotlarni ko`rish\n/1oy - oylik ma`lumotlarini olish uchun komandasini bosing!")


