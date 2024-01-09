from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
class AdminClasses(StatesGroup):
    login_admin = State()
    keldi = State()
    ketdi = State()
dp = Dispatcher(bot, storage=MemoryStorage())
