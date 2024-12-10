"""Loading bot and dispatcher."""

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import Config


bot = Bot(token=Config.bot_token)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, storage=MemoryStorage(), loop=loop)