from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get():
    """Creating inline keyboard for articles"""
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_btn_allowance = InlineKeyboardButton('Пособие для родителей', callback_data='allowance')
    inline_btn_article1 = InlineKeyboardButton('Агрессивный ребенок', callback_data='article1')
    inline_btn_article2 = InlineKeyboardButton('Давай дружить', callback_data='article2')
    inline_btn_article3 = InlineKeyboardButton('Дети и гаджеты', callback_data='article3')
    inline_btn_article4 = InlineKeyboardButton('Дизграфия', callback_data='article4')
    inline_btn_article5 = InlineKeyboardButton('Как воспитать в ребенке здоровую уверенность', callback_data='article5')
    inline_btn_article6 = InlineKeyboardButton('Как помочь подростку', callback_data='article6')
    inline_btn_article7 = InlineKeyboardButton('Мой ребенок готов к школе', callback_data='article7')
    inline_btn_article8 = InlineKeyboardButton('Причины самоповреждающего поведения', callback_data='article8')
    inline_btn_article9 = InlineKeyboardButton('Ребенок остро реагирует на критику', callback_data='article9')
    inline_btn_article10 = InlineKeyboardButton('Роль отца в воспитании девочки', callback_data='article10')
    inline_btn_article11 = InlineKeyboardButton('Что такое психосоматика', callback_data='article11')
    inline_kb.add(
        inline_btn_allowance, inline_btn_article1, inline_btn_article2, inline_btn_article3,
        inline_btn_article4, inline_btn_article5, inline_btn_article6, inline_btn_article7,
        inline_btn_article8, inline_btn_article9, inline_btn_article10, inline_btn_article11,
    )
    return inline_kb
