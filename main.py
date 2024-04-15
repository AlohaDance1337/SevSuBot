from aiogram import Bot, Dispatcher
from core.utils import get_token
from core.handlers import routers

import asyncio
import logging

logging.basicConfig(filename="bot_logs.log", level=logging.INFO, filemode="w")


async def main():
    bot = Bot(token=get_token("TG_Bot"))
    dp = Dispatcher()
    dp.include_routers(*routers)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
