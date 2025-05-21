from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from settings import URLS


def get():
    """Creating an inline keyboard for the general link of VK group."""
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text='Перейти по ссылке',
        url=URLS['VK_GROUP'])
    )
    return builder.as_markup()
