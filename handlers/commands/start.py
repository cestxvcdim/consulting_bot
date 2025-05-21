"""Send menu with options after typing /start command."""
import asyncio

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from db_logic.services import get_user_by_tg_id, create_user
from logger import setup_logger

start_router = Router()

logger = setup_logger(__name__)


@start_router.message(CommandStart())
async def start(message: Message) -> None:
    from markups import start_markup

    user = await asyncio.to_thread(get_user_by_tg_id, message.chat.id)
    if user is None:
        try:
            data = {'chat_id': message.chat.id}
            await asyncio.to_thread(create_user, **data)
        except Exception as e:
            logger.error(f"Ошибка при вызове create_user:\n{e}")

    await message.answer("Здравствуйте! Выберите опцию:", reply_markup=start_markup.get())
