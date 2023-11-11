from aiogram import types
from aiogram.filters import Filter

class isAdminMessage(Filter):
    
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in int(config.get_accountent())
    
class isAdminCallback(Filter):
    
    async def __call__(self, call:types.CallbackQuery) -> bool:
        return call.from_user.id in int(config.get_accountent())
    
class isUserMessage(Filter):
    
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id not in int(config.get_accountent())
    
class isUserCallback(Filter):
    
    async def __call__(self, call:types.CallbackQuery) -> bool:
        return call.from_user.id not in int(config.get_accountent())
