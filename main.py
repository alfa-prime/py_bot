from aiogram.utils import executor

from app.handlers import dp
from app.bot import logger


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()
    logger.info('Storage close')


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown)
    except Exception as e:
        print(e, "CHECK BOT_TOKEN SETTINGS IN .env")

