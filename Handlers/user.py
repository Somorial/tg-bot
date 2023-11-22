from aiogram import types
from loader import dp, bot
from aiogram.filters import Command
from data import config, db
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
from filters import isAdminCallback, isAdminMessage, isUserCallback, isUserMessage

from states import WorkDay

from keyboards import start_menu_for_user, day_mark

import logging

logging.basicConfig(level=logging.INFO)

@dp.callback_query(isUserCallback(), F.data == 'back_to_menu')
@dp.message(Command(commands=['start']), isUserMessage())
async def on_start(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id, 
                           text=f'Добрый день, {message.from_user.username}\nВыбери пункт в меню', 
                           reply_markup=start_menu_for_user())
    
@dp.callback_query(isusercallback(), F.data == 'day_start')
async def day_start(call:types.CallbackQuery, state:FSMContext):
    await bot.send_message(text='Отметиться на рабочем месте',
                           chat_id=call.from_user.id,
                           reply_markup=day_mark())
    await state.set_state(WorkDay.choosing_what_next)

@dp.callback_query(isUserCallback(), WorkDay.choosing_what_next)
async def check(call:types.CallbackQuery, state:FSMContext):
    await state.update_data(what_next=call.data)
    user_data = await state.get_data()
    work_location = types.Location()
    if user_data['what_next'] == 'yes':
        #TODO: Добавить функцию проверки на валид
        pass
    