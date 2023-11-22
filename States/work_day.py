from aiogram.fsm.state import State, StatesGroup

class WorkDay(StatesGroup):
    choosing_what_next = State()