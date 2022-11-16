import asyncio
import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage, loop=asyncio.get_event_loop())
