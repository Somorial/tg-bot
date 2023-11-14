from aiogram import types
from loader import dp, bot
from aiogram.filters import Command
from data import config, db
from aiogram import Router, F
from aiogram.enums.parse_mode import ParseMode
from filters import isAdminCallback, isAdminMessage, isUserCallback, isUserMessage

from keyboards import start_menu

import logging

logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']), isUserMessage())
async def on_start(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id, 
                           text=f'Добрый день, {message.from_user.username}\nВыбери пункт в меню', 
                           reply_markup=start_menu())
    