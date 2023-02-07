from aiogram import Bot, Dispatcher
# from aiogram.fsm.storage.redis import RedisStorage
# from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from settings import settings

# storage = RedisStorage.from_url(settings.db.redis)
storage = MemoryStorage()
bot = Bot(settings.bots.bot_token)
dp = Dispatcher(storage=storage)
