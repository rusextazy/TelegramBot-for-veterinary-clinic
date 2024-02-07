import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.utils.config import Config, load_config
from app.handlers.user import commands, content, goods_for_pets
from app.callbacks.user import doctors_button, application_for_admission

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('БОТ ЗАПУЩЕН')

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(content.router)
    dp.include_router(goods_for_pets.router)
    dp.include_router(doctors_button.router)
    dp.include_router(application_for_admission.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
