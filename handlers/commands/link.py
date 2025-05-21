"""Send a link on VK group after typing /link command"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

link_router = Router()


@link_router.message(Command('link'))
async def get_link(message: Message) -> None:
    from markups import link_markup

    await message.answer('Родительская гостиная ВКонтакте', reply_markup=link_markup.get())
