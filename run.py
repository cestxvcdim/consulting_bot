"""This file is intended to collect the entire project and run it"""

from aiogram import executor
from db_logic.setup_db import init_db


if __name__ == '__main__':
    from handlers import dp
    init_db()
    executor.start_polling(dp, skip_updates=True)
