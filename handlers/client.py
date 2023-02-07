from aiogram import Dispatcher
from aiogram.types import Message


async def start_message(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name} \n\nВ этом боте ты найдёшь инструменты для '
                         f'самопознания, книгу о твоём предназначении, волшебную музыкальную атмосферу, аудиокниги, '
                         f'подкасты и сериал «Активация Гениальности».\n☯\nЕсли ты чувствуешь искреннее желание '
                         f'познать себя, раскрыть свои дары и реализовать свою гениальность в жизни – ты '
                         f'находишься в нужный момент, в правильном месте\n⚛\nВыбирай любую кнопку из меню и '
                         f'отправляйся в незабываемое путешествие созерцания и самопознания�')


def register_handlers_client(dp: Dispatcher):
    dp.message.register(start_message, commands=['start'])
