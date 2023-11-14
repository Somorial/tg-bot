from aiogram import types
from aiogram.filters import Filter

from data import config

class isAdminMessage(Filter):
    
    async def __call__(self, message: types.Message) -> bool:
       return message.from_user.id == int(config.get_accountent())
   
class isAdminCallback(Filter):
    
    async def __call__(self, call:types.CallbackQuery) -> bool:
        return message.from_user.id == int(config.get_accountent())
    
class isUserMessage(Filter):
    
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id != int(config.get_accountent())
    
class isUserCallback(Filter):
    
    async def __call__(self, call:types.CallbackQuery) -> bool:
      return message.from_user.id != int(config.get_accountent())
