from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from settings import URLS


def get():
    """Creating an inline keyboard of the base menu."""
    builder = InlineKeyboardBuilder()

    inline_url_1 = InlineKeyboardButton(text='Нормативно-правовая база КЦ', url=URLS['KC_BASE'])
    inline_url_2 = InlineKeyboardButton(text='Запись на консультацию', url=URLS['CONSULTING_APPOINTMENT'])
    inline_btn_1 = InlineKeyboardButton(text='Полезные материалы', callback_data='materials')
    inline_url_3 = InlineKeyboardButton(text='Портал «Растим детей»', url=URLS['PORTAL'])
    inline_btn_2= InlineKeyboardButton(text='Задать вопрос ассистенту', callback_data='faq')
    inline_url_4 = InlineKeyboardButton(text='Оценка качества предоставляемых услуг', url=URLS['YANDEX_FORM'])
    inline_url_5 = InlineKeyboardButton(text='Отзыв о деятельности консультанта', url=URLS['FEEDBACK_TO_EXPERT'])

    builder.row(
        inline_url_1,
        inline_url_2,
        inline_btn_1,
        inline_url_3,
        inline_btn_2,
        inline_url_4,
        inline_url_5,
    )
    builder.adjust(1)

    return builder.as_markup()
