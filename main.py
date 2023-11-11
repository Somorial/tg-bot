from handlers import dp, bot
import asyncio
from data import db

async def start():
    await db.create_tables()
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())