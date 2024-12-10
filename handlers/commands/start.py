"""Send menu with options after typing /start command"""

from aiogram.dispatcher.filters import CommandStart
from aiogram import types

from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def send_welcome(message: types.Message):
    from markups import start_markup

    await message.reply("Здравствуйте! Выберите опцию:", reply_markup=start_markup.get())
