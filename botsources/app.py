import logging
from aiogram import executor
from botsources.namespace import dp
from . import handlers


logger = logging.getLogger(__name__)


def launch_bot():
    logging.basicConfig(level=logging.INFO)
    try:
        executor.start_polling(dispatcher=dp, skip_updates=True)
    except Exception as e:
        logger.error(e)
