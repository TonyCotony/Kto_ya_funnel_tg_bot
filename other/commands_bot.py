from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='Начани работу со мной'
        ),
        BotCommand(
            command='help',
            description='Если вдруг нужна помощь'
        ),
        BotCommand(
            command='cancel',
            description='Почти перезагрузка'
        ),
        BotCommand(
            command='admin',
            description='Если Вы админ'
        )
    ]

    await bot.set_my_commands(command, BotCommandScopeDefault())


async def set_admin_commands(bot: Bot):
    command = [
        BotCommand(
            command='объект',
            description='добавить объект'
        ),
        BotCommand(
            command='группа',
            description='добавить группу'
        ),
        BotCommand(
            command='удалить',
            description='почти перезагрузка'
        )
    ]

    await bot.set_my_commands(command, BotCommandScopeDefault())
