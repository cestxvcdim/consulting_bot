from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get():
    """Creating inline keyboard for general link of VK group"""
    inline_kb = InlineKeyboardMarkup(row_width=1)
    link = InlineKeyboardButton('Перейти по ссылке', url='https://vk.com/roditelgostinaya')
    inline_kb.add(link)
    return inline_kb