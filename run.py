"""This file is intended to collect the entire project and run it"""

import asyncio

from handlers.commands.start import start_router
from handlers.commands.link import link_router

from handlers.main import main_router

from loader import bot, dp
from logger import setup_logger

logger = setup_logger(__name__)


async def run_main():
    logger.info('Starting a bot...')
    dp.include_router(start_router)
    dp.include_router(link_router)
    dp.include_router(main_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(run_main())
