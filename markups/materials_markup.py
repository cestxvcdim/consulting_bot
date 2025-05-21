from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get():
    """Creating an inline keyboard for articles."""
    builder = InlineKeyboardBuilder()

    inline_btn_allowance = InlineKeyboardButton(text='Пособие для родителей', callback_data='allowance')
    inline_btn_article1 = InlineKeyboardButton(text='Агрессивный ребенок', callback_data='article1')
    inline_btn_article2 = InlineKeyboardButton(text='Давай дружить', callback_data='article2')
    inline_btn_article3 = InlineKeyboardButton(text='Дети и гаджеты', callback_data='article3')
    inline_btn_article4 = InlineKeyboardButton(text='Дизграфия', callback_data='article4')
    inline_btn_article5 = InlineKeyboardButton(text='Как воспитать в ребенке здоровую уверенность', callback_data='article5')
    inline_btn_article6 = InlineKeyboardButton(text='Как помочь подростку', callback_data='article6')
    inline_btn_article7 = InlineKeyboardButton(text='Мой ребенок готов к школе', callback_data='article7')
    inline_btn_article8 = InlineKeyboardButton(text='Причины самоповреждающего поведения', callback_data='article8')
    inline_btn_article9 = InlineKeyboardButton(text='Ребенок остро реагирует на критику', callback_data='article9')
    inline_btn_article10 = InlineKeyboardButton(text='Роль отца в воспитании девочки', callback_data='article10')
    inline_btn_article11 = InlineKeyboardButton(text='Что такое психосоматика', callback_data='article11')

    builder.row(
        inline_btn_allowance,
        inline_btn_article1,
        inline_btn_article2,
        inline_btn_article3,
        inline_btn_article4,
        inline_btn_article5,
        inline_btn_article6,
        inline_btn_article7,
        inline_btn_article8,
        inline_btn_article9,
        inline_btn_article10,
        inline_btn_article11,
    )
    builder.adjust(1)

    return builder.as_markup()
