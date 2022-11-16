from aiogram import types
from ..namespace import *
from celery_.tasks import send_hello


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    send_hello.delay()
    await message.answer("asdada")
