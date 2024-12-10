from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import URLS


def get():
    """Creating inline keyboard of base menu"""
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_url_1 = InlineKeyboardButton('Нормативно-правовая база КЦ', url=URLS['kc_base'])
    inline_url_2 = InlineKeyboardButton('Запись на консультацию', url=URLS['consulting_appointment'])
    inline_btn_1 = InlineKeyboardButton('Полезные материалы', callback_data='materials')
    inline_url_3 = InlineKeyboardButton('Портал «Растим детей»', url=URLS['portal'])
    inline_btn_2= InlineKeyboardButton('Задать вопрос ассистенту', callback_data='faq')
    inline_url_4 = InlineKeyboardButton('Оценка качества предоставляемых услуг', url=URLS['yandex_form'])
    inline_url_5 = InlineKeyboardButton('Отзыв о деятельности консультанта', url=URLS['feedback_to_consultant'])

    inline_kb.add(inline_url_1, inline_url_2, inline_url_3,
        inline_url_4, inline_url_5, inline_btn_1, inline_btn_2)
    return inline_kb
