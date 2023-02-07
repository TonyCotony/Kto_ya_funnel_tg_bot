from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='Начни работу со мной'
        ),
        BotCommand(
            command='help',
            description='Если вдруг нужна помощь'
        ),
        BotCommand(
            command='cancel',
            description='Если что-то идет не так'
        )
    ]

    await bot.set_my_commands(command, BotCommandScopeDefault())

#
# async def set_admin_commands(bot: Bot):
#     command = [
#         BotCommand(
#             command='объект',
#             description='добавить объект'
#         ),
#         BotCommand(
#             command='группа',
#             description='добавить группу'
#         ),
#         BotCommand(
#             command='удалить',
#             description='почти перезагрузка'
#         )
#     ]
#
#     await bot.set_my_commands(command, BotCommandScopeDefault())
