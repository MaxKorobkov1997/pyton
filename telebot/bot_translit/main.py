import asyncio
import config
import logging
from aiogram import Bot, Dispatcher
from hendlers import hendlers
from callback import calbak
from bot_start import star

bot = Bot(token=config.BOT_TOKEN)

    
async def main():
    dp = Dispatcher()
    dp.include_routers(star,
                       hendlers,
                       calbak)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except:
        KeyboardInterrupt()
