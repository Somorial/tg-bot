from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import config

def start_menu_for_user():
    keyboard =  InlineKeyboardBuilder()
    buttons = {
        'Начало рабочего дня':'day_start',
        'Конец рабочего дня':'day_end',
        'Обьявления':'ads',
        'Статистика':'stat'
    }
    for key, value in buttons.items():
        keyboard.button(text=key, callback_data=value)
    keyboard.adjust(2)
    return keyboard.as_markup()

def day_mark():
    keyboard = InlineKeyboardBuilder()
    buttons = {
        '✔️':'yes',
        '❌':'back_to_menu',
    }
    for key, value in buttons.items():
        keyboard.button(text=key, callback_data=value)
    return keyboard.as_markup()