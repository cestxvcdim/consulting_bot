"""Senf link on VK group after typing /link command"""

from aiogram import types
from loader import dp, bot


@dp.message_handler(commands=['link'])
async def send_link(message: types.Message):
    from markups import link_markup

    await bot.send_message(message.chat.id, 'Родительская гостиная ВКонтакте', reply_markup=link_markup.get())
