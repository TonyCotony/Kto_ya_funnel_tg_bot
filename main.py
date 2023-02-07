import asyncio
import logging
import time

from aiogram import Bot

from create_bot import dp, bot
from handlers import admin, client
from other.commands_bot import set_commands
from settings import settings

logger = logging.getLogger(__name__)


async def start_bot(bot: Bot):
    await set_commands(bot)
    # await bot.send_message(settings.user.admin_id, text='Bot started')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.user.admin_id, text='Bot turned off')


# async def create_pool(user, password, database, host):
#     return await asyncpg.create_pool(user=user, password=password, database=database,
#                                      host=host, port=5432, command_timeout=60)


async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    dp.startup.register(start_bot)
    client.register_handlers_client(dp)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())
