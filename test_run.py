"""
This file is intended for fast run and test new functionality.
"""

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from openai import OpenAI

import logging
from utils import get_gpt_response

from config import Config
from db_logic.setup_db import init_db

# Set bot token and client with API key
BOT_TOKEN = Config.bot_token
API_KEY = Config.api_key
client = OpenAI(api_key=API_KEY)

# Set logging
logging.basicConfig(level=logging.INFO)

# Initializing bot and dispatcher
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    from markups import start_markup

    await message.reply("Здравствуйте! Выберите опцию:", reply_markup=start_markup.get())

@dp.message_handler(commands=['link'])
async def send_link(message: types.Message):
    from markups import link_markup

    await bot.send_message(message.chat.id, 'Родительская гостиная ВКонтакте', reply_markup=link_markup.get())


@dp.callback_query_handler(lambda c: c.data)
async def process_start(callback_query: types.CallbackQuery):
    btn_id = callback_query.data

    if btn_id == 'materials':
        # redirect to page with articles
        await useful_materials(callback_query)

    elif btn_id == 'faq':
        # start to chat with AI Assistant
        await bot.send_message(callback_query.from_user.id, 'Напишите ваш вопрос, наш ассистент ответит вам.')
        # confirm, that callback is answered
        await bot.answer_callback_query(callback_query.id)

    else:
        await process_materials(callback_query)

@dp.callback_query_handler(lambda c: c.data)
async def useful_materials(callback_query: types.CallbackQuery):
    from markups import materials_markup

    await bot.send_message(callback_query.from_user.id, 'Ознакомиться с материалами:', reply_markup=materials_markup.get())

@dp.callback_query_handler(lambda c: c.data)
async def process_materials(callback_query: types.CallbackQuery):
    from utils import CB_DATA

    btn_id = callback_query.data
    # generate file name
    file_name = CB_DATA[btn_id]
    if btn_id == 'allowance':
        file_name = 'Электронное ' + file_name.lower() + '.pdf'
    else:
        file_name += '.docx'

    # Send file to user
    with open(f'./files/{file_name}', 'rb') as f:
        await bot.send_document(callback_query.from_user.id, f)
    await bot.answer_callback_query(callback_query.id) # confirm, that callback is answered

@dp.message_handler(content_types=['text'])
async def gpt(message: types.Message):
    prompt = message.text # user question/statement
    response = get_gpt_response(prompt, client) + '\n' # get response from GPT
    end_message = '\nЕсли вы не нашли ответ на вопрос обратитесь в консультационный центр СОВА.'
    await bot.send_message(message.chat.id, response + end_message) # answer to user

if __name__ == '__main__':
    # init_db()
    executor.start_polling(dp, skip_updates=True)
