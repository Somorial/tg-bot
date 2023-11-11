from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from data import config

bot = Bot(token=config.get_token())
dp = Dispatcher(storage=MemoryStorage())
