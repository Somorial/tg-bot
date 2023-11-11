from aiogram import types
from loader import dp, bot
from aiogram.filters import Command
from data import config, db
from aiogram import Router, F
from aiogram.enums.parse_mode import ParseMode

import logging

logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def on_start(message):
    await bot.send_message(chat_id=message.from_user.id, text='Ку')