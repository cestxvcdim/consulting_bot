import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.utils.chat_action import ChatActionSender

from loader import bot

main_router = Router()


@main_router.callback_query(F.data == 'faq')
async def faq(query: CallbackQuery):
    await query.message.answer('Напишите ваш вопрос, наш ассистент ответит вам.')


@main_router.callback_query(F.data == 'materials')
async def useful_materials(query: CallbackQuery):
    from markups import materials_markup

    await query.message.answer('Ознакомиться с материалами:', reply_markup=materials_markup.get())


@main_router.callback_query(F.data)
async def process_materials(query: CallbackQuery):
    from services import get_file_name

    message = query.message

    btn_data = query.data
    file_name = get_file_name(btn_data)
    file_path = f'./files/{file_name}'

    async with ChatActionSender.upload_document(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(0.2)
        await message.answer_document(FSInputFile(file_path))


@main_router.message(F.text)
async def gpt(message: Message):
    from openai import OpenAI
    from utils import get_gpt_response
    from settings import OPENAI_API_KEY

    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = message.text  # User question/statement.
    response = get_gpt_response(prompt, client) + '\n'  # Get response from GPT.
    end_message = '\nЕсли вы не нашли ответ на вопрос обратитесь в консультационный центр СОВА.'
    await message.answer(response + end_message)  # Answer to user.
