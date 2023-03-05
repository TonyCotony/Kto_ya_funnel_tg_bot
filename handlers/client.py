import asyncio

from aiogram import Dispatcher, Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery, ContentType

from keyboards.client_kb import client_menu_kb, client_back_kb, client_back_n_feedback_kb, serials_kb, podcasts_kb, \
    siddhi_kb, shadows_kb
from other.dbactions import DBActions
from settings import settings


class Funnel(StatesGroup):
    main_change = State()
    get_feedback = State()
    serial_buy = State()
    shadows_buy = State()
    siddhi_buy = State()


async def start_message(message: Message, state: FSMContext):
    await message.answer(f'Привет, {message.from_user.first_name} \n\nВ этом боте ты найдёшь инструменты для '
                         f'самопознания, книгу о твоём предназначении, волшебную музыкальную атмосферу, аудиокниги, '
                         f'подкасты и сериал «Активация Гениальности».\n☯\nЕсли ты чувствуешь искреннее желание '
                         f'познать себя, раскрыть свои дары и реализовать свою гениальность в жизни – ты '
                         f'находишься в нужный момент, в правильном месте\n⚛\nВыбирай любую кнопку из меню и '
                         f'отправляйся в незабываемое путешествие созерцания и самопознания�')
    await asyncio.sleep(15)
    new_client = DBActions()
    new_client.add_new_user(message)
    await state.set_state(Funnel.main_change)
    await message.answer('Выбери свой путь:', reply_markup=client_menu_kb)


async def start_callback(call: CallbackQuery, state: FSMContext):
    await state.set_state(Funnel.main_change)
    await call.message.answer('Выбери свой путь:', reply_markup=client_menu_kb)


async def main_menu_navigate(call: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.answer_callback_query(call.id)
    update_info = DBActions()
    if call.data.startswith('client_'):
        if call.data == 'client_meet':
            update_info.add_new_visited_section('Знакомство', call.from_user.id)
            # Возможно сделать отправку видео, через базу
            await call.message.edit_text('https://youtube.com/watch?v=zV7lrWumc7U&si=EnSIkaIECMiOmarE \n'
                                         'Тут есессно надо либо отправлять видео(в чем я не уверен), либо ютубчик ссылку',
                                         reply_markup=client_back_kb)

            # await bot.edit_message_text('https://youtube.com/watch?v=zV7lrWumc7U&si=EnSIkaIECMiOmarE \n'
            #                             'Тут есессно надо либо отправлять видео(в чем я не уверен), либо ютубчик ссылку',
            #                             reply_markup=client_back_kb)
            # await call.message.answer('https://youtube.com/watch?v=zV7lrWumc7U&si=EnSIkaIECMiOmarE \n'
            #                           'Тут есессно надо либо отправлять видео(в чем я не уверен), либо ютубчик ссылку',
            #                           reply_markup=client_back_kb)
        elif call.data == 'client_music_atmo':
            update_info.add_new_visited_section('Музыка', call.from_user.id)
            await call.message.edit_text('Приветствую тебя в этом разделе\n☀🎧 Здесь ты найдешь более 1.300 Треков и '
                                         'отборных Сетов мелодичной электронной музыки, медитативные композиции, '
                                         'плейлист с мантрами и аудиокнигами на духовные темы.\n\n⚛ Весь этот контент '
                                         'я годами искал. фильтровал и выгружал в свои телеграмм каналы. Так, '
                                         'что у тебя есть прекрасная возможность быть со мной на одной '
                                         'волне)\nПодписывайся и наслаждайся.\n\nПлейлист для созерцания, практик,'
                                         'творчества или отдыха:https://t.me/aaooommm \n\nНасладиться потоком '
                                         'электронной музыки: https://t.me/vibration_s \n\nЛЮБИШЬ МАНТРЫ? – '
                                         'Пожалуйста: https://t.me/sat_chit \n\nЕСТЬ ИСКРЕННИЙ ВОПРОС? Источник '
                                         'Мудрости - Твой Верный Слуга: https://t.me/brah_man\n\n🌐так же у меня есть '
                                         'YouTube, я им совершенно не занимался, но возможно в ближайшем будущем это '
                                         'изменится;) \nhttps://www.youtube.com/@ktoya_space',
                                         reply_markup=client_back_kb)
        elif call.data == 'client_book':
            update_info.add_new_visited_section('Книга KtoYa', call.from_user.id)
            await call.message.edit_text('В этом разделе ты можешь скачать мою книгу: «KtoYa. Путь Самопознания и '
                                         'Предназначения». Я сделал ее максимально содержательной, и в то же время '
                                         'краткой, чтобы на погружение не уходило больше 1 часа. \n\nВ этой книге я '
                                         'оставил фрагменты осознаний и ответы на вопросы о природе человека, '
                                         'гениальности и предназначении. \n\nТы найдешь в ней практики самопознания, '
                                         'которые помогут быть осознанным в каждый момент времени, в любых ситуациях. '
                                         'Эта книга – квинтэссенция моего жизненного опыта и глубокого погружения в '
                                         'самую суть вопросов о реализации и гармонии во внешнем и внутреннем мире '
                                         'каждого человека на этой планете. В ней есть ключи, которые погружают в '
                                         'тайну жизни и помогают осознать путь для реализации твоего предназначения. '
                                         '\n\nСкачивай книгу ниже и после прочтения напиши пожалуйста отзыв, '
                                         'твоя обратная связь будет лучшей благодарностью за мой труд.',
                                         reply_markup=client_back_n_feedback_kb)

        elif call.data == 'client_serial':
            update_info.add_new_visited_section('Сериал', call.from_user.id)
            # доделать
            # await call.message.answer('https://www.youtube.com/watch?v=da9v6PCm7Y8&ab_channel=%D0%9F%D0%BE%D0%B3'
            #                           '%D0%BD%D0%B0%D0%BB%D0%B8%21 \n'
            #                           'Добро пожаловать в сериал.\n\nЗдесь Ты узнаешь:')
            # await asyncio.sleep(10)
            await call.message.edit_text('https://www.youtube.com/watch?v=da9v6PCm7Y8&ab_channel=%D0%9F%D0%BE%D0%B3'
                                         '%D0%BD%D0%B0%D0%BB%D0%B8%21 \n'
                                         'Добро пожаловать в сериал.\n\nЗдесь Ты узнаешь:'
                                         'Уже посмотрел трейлер и хочешь узнать что дальше?',
                                         reply_markup=serials_kb)

        elif call.data == 'client_feedback':
            update_info.add_new_visited_section('Отзывы', call.from_user.id)
            # need query from db to send feedback
            await call.message.edit_text('Отзывы будет удобно посмотреть по ссылке: https://t.me/TonyCotonyChannel',
                                         reply_markup=client_back_kb)
        elif call.data == 'client_my_contacts':
            update_info.add_new_visited_section('Контакты', call.from_user.id)
            contacts = update_info.get_contacts()
            await call.message.edit_text(f'Вот все мои контакты, друг:\n{contacts}',
                                         reply_markup=client_back_kb)
            # need to send contacts
        elif call.data == 'client_podcasts':
            update_info.add_new_visited_section('Подкасты', call.from_user.id)
            await call.message.edit_text('У меня есть два очень сильных подкаста\n\n'
                                         '- Тени и Дары\n\n'
                                         '- Сиддхи\n\n'
                                         'О чем хочешь узнать подробнее в первую очередь?',
                                         reply_markup=podcasts_kb)
    elif call.data == 'back_2_menu':
        await call.message.edit_text('Выбери свой путь, друг:', reply_markup=client_menu_kb)

    else:
        if call.data == 'shadows':
            await call.message.edit_text('Серия подкастов о знаках, тенях и дараках',
                                         reply_markup=shadows_kb)
        elif call.data == 'siddhi':
            await call.message.edit_text('Серия подкастов о Сиддхи и ситхах, братан, не знаю что это:)',
                                         reply_markup=siddhi_kb)

        elif call.data == 'buy_shadows':
            await shadows_buy(call, bot, state)

        elif call.data == 'buy_siddhi':
            await siddhi_buy(call, bot, state)


async def get_feedback(call: CallbackQuery, state: FSMContext):
    await state.set_state(Funnel.get_feedback)
    await call.message.answer(f'Мой дорогой {call.from_user.first_name}\n'
                              f'Отзывы - это то, что вдохновляет и двигает мир вперед, и я как часть этого мира с '
                              f'большой благодарностью приму твой отзыв. Просто напиши сообщение и отправь его мне, '
                              f'а я размещу его на канале с отзывами 🙏')


async def save_feedback(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    feedback = DBActions()
    feedback.add_new_visited_section('отзыв оставлен', message.from_user.id)
    await bot.send_message(settings.user.admin_id, message.text)
    await message.answer('Благодарю тебя, мой друг!')
    await start_callback(message, state)


async def serial_buy(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.answer('Над этим сериалом я работа 30 лет и он просто бомба, честно говоря')
    await asyncio.sleep(5)
    await state.set_state(Funnel.serial_buy)
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title='Сериал "Активация Гениальности"',
        description='То что нужно тебе, чтобы активировать свою внутреннюю силу',
        payload='pay-for-serials',
        provider_token=settings.bots.paid_token,  # PayMaster Test: 1744374395:TEST:4b2bc4c19ded5ae1117a
        currency='rub',  # youkassa: 381764678:TEST:44198
        prices=[
            LabeledPrice(
                label='Доступ к сериалу навсегда',
                amount=1000000
            ),
            LabeledPrice(
                label='Тут можно поставить дополнительный контент или не явные преимущества',
                amount=0
            ),
            LabeledPrice(
                label='Можно даже чаевые поставить, либо полностью от них отказаться',
                amount=0
            )
        ],
        # max_tip_amount=5000,
        # suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='ktoyabot',  # в случае, если счет отправлен ошибочно другому человеку,
        # то при нажатии кнопки заплатить он просто перейдет в чат к боу, а не на страницу оплаты
        # provider_data=None,
        photo_url='https://downloader.disk.yandex.ru/preview/9c1bc006fbbecf2f6c7f209b4a586a08103ba0f067272189b24f41b934a8dc66/635c2d9e/29512FjS8phVEg3ep65Vszx_G0-WniKvQtHF4bAowJGLDZHSv-Onv7S1wGtTK-3YvzV0OwoLyONZsnFIHK402w%3D%3D?uid=0&filename=Estate_helper_bot.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x932',
        photo_size=1280,
        photo_width=1280,
        photo_height=1280,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        # need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        # disable_notification=False,
        # protect_content=False,
        # reply_to_message_id=None,
        # allow_sending_without_reply=True,
        # reply_markup=None
        # reply_markup=payment_keyboard
    )
    await asyncio.sleep(20)
    await call.message.answer('Если хочешь посмотреть, что у меня еще есть, можешь вернуться в главное меню',
                              reply_markup=client_back_kb)


async def serial_pre_buy_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    print(pre_checkout_query)
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def serial_successful_payment(message: Message, bot: Bot, state: FSMContext):
    msg = f'🎉🎉🎉Поздравляю! \nДля тебя будущее наступает уже сегодня!\n ' \
          f'я буду отправлять тебе видео по очереди(мб тебе откроется доп пункт меню или просто ссылка на ютьюб ' \
          f'по ссылке)'
    print(serial_successful_payment)
    update_buy = DBActions()
    update_buy.serial_buy(message.from_user.id)

    await state.clear()
    await message.answer(msg)
    await bot.send_message(settings.user.admin_id, f'payment for {message.successful_payment.total_amount // 100} '
                                                   f'{message.successful_payment.currency}. '
                                                   f'from {message.from_user.id} '
                                                   f'by @{message.from_user.username} was successful')
    await asyncio.sleep(10)
    await start_message(message, state)


async def shadows_buy(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.answer('Над этим подкастом я кропел день и ночь, с любовью и увренностью,'
                              ' что он сможет сделать тебя сильнее, и он просто бомба, честно говоря')
    await asyncio.sleep(5)
    await state.set_state(Funnel.shadows_buy)
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title='Подкаст "Тени и Дары"',
        description='То что нужно тебе, чтобы активировать свою внутреннюю силу',
        payload='pay-for-serials',
        provider_token=settings.bots.paid_token,  # PayMaster Test: 1744374395:TEST:4b2bc4c19ded5ae1117a
        currency='rub',  # youkassa: 381764678:TEST:44198
        prices=[
            LabeledPrice(
                label='Доступ к подкасту',
                amount=1000000
            ),
            LabeledPrice(
                label='Тут можно поставить дополнительный контент или не явные преимущества',
                amount=0
            ),
            LabeledPrice(
                label='Доступ к новым подкастам в этой ветке',
                amount=0
            )
        ],
        # max_tip_amount=5000,
        # suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='ktoyabot',  # в случае, если счет отправлен ошибочно другому человеку,
        # то при нажатии кнопки заплатить он просто перейдет в чат к боу, а не на страницу оплаты
        # provider_data=None,
        photo_url='https://downloader.disk.yandex.ru/preview/9c1bc006fbbecf2f6c7f209b4a586a08103ba0f067272189b24f41b934a8dc66/635c2d9e/29512FjS8phVEg3ep65Vszx_G0-WniKvQtHF4bAowJGLDZHSv-Onv7S1wGtTK-3YvzV0OwoLyONZsnFIHK402w%3D%3D?uid=0&filename=Estate_helper_bot.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x932',
        photo_size=1280,
        photo_width=1280,
        photo_height=1280,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        # need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        # disable_notification=False,
        # protect_content=False,
        # reply_to_message_id=None,
        # allow_sending_without_reply=True,
        # reply_markup=None
        # reply_markup=payment_keyboard
    )
    await asyncio.sleep(20)
    await call.message.answer('Если хочешь посмотреть, что у меня еще есть, можешь вернуться в главное меню',
                              reply_markup=client_back_kb)


async def shadow_pre_buy_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    print(pre_checkout_query)
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def shadow_successful_payment(message: Message, bot: Bot, state: FSMContext):
    msg = f'🎉🎉🎉Поздравляю! \nДля тебя будущее наступает уже сегодня!\n ' \
          f'я буду отправлять тебе подкасты по очереди(мб тебе откроется доп пункт меню или просто ссылка на ютьюб ' \
          f'по ссылке)\nВот еще ссылка на закрытый канал: ссылка'
    print(serial_successful_payment)
    update_buy = DBActions()
    update_buy.shadow_buy(message.from_user.id)

    await state.clear()
    await message.answer(msg)
    await bot.send_message(settings.user.admin_id, f'payment for {message.successful_payment.total_amount // 100} '
                                                   f'{message.successful_payment.currency}. '
                                                   f'from {message.from_user.id} '
                                                   f'by @{message.from_user.username} was successful')
    await asyncio.sleep(10)
    await start_message(message, state)


async def siddhi_buy(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.answer('Над этим подкастом я кропел день и ночь, с любовью и увренностью,'
                              ' что он сможет сделать тебя сильнее, и он просто бомба, честно говоря')
    await asyncio.sleep(5)
    await state.set_state(Funnel.siddhi_buy)
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title='Подкаст "Сиддхи"',
        description='То что нужно тебе, чтобы активировать свою внутреннюю силу',
        payload='pay-for-serials',
        provider_token=settings.bots.paid_token,  # PayMaster Test: 1744374395:TEST:4b2bc4c19ded5ae1117a
        currency='rub',  # youkassa: 381764678:TEST:44198
        prices=[
            LabeledPrice(
                label='Доступ к подкасту siddhi',
                amount=1000000
            ),
            LabeledPrice(
                label='Тут можно поставить дополнительный контент или не явные преимущества',
                amount=0
            ),
            LabeledPrice(
                label='Доступ к новым подкастам в этой ветке',
                amount=0
            )
        ],
        # max_tip_amount=5000,
        # suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='ktoyabot',  # в случае, если счет отправлен ошибочно другому человеку,
        # то при нажатии кнопки заплатить он просто перейдет в чат к боу, а не на страницу оплаты
        # provider_data=None,
        photo_url='https://downloader.disk.yandex.ru/preview/9c1bc006fbbecf2f6c7f209b4a586a08103ba0f067272189b24f41b934a8dc66/635c2d9e/29512FjS8phVEg3ep65Vszx_G0-WniKvQtHF4bAowJGLDZHSv-Onv7S1wGtTK-3YvzV0OwoLyONZsnFIHK402w%3D%3D?uid=0&filename=Estate_helper_bot.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x932',
        photo_size=1280,
        photo_width=1280,
        photo_height=1280,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        # need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        # disable_notification=False,
        # protect_content=False,
        # reply_to_message_id=None,
        # allow_sending_without_reply=True,
        # reply_markup=None
        # reply_markup=payment_keyboard
    )
    await asyncio.sleep(20)
    await call.message.answer('Если хочешь посмотреть, что у меня еще есть, можешь вернуться в главное меню',
                              reply_markup=client_back_kb)


async def siddhi_pre_buy_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    print(pre_checkout_query)
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def siddhi_successful_payment(message: Message, bot: Bot, state: FSMContext):
    msg = f'🎉🎉🎉Поздравляю! \nДля тебя будущее наступает уже сегодня!\n ' \
          f'я буду отправлять тебе подкасты по очереди(мб тебе откроется доп пункт меню или просто ссылка на ютьюб ' \
          f'по ссылке)\nВот еще ссылка на закрытый канал: ссылка'
    print(serial_successful_payment)
    update_buy = DBActions()
    update_buy.siddhi_buy(message.from_user.id)
    await state.clear()
    await message.answer(msg)
    await bot.send_message(settings.user.admin_id, f'payment for {message.successful_payment.total_amount // 100} '
                                                   f'{message.successful_payment.currency}. '
                                                   f'from {message.from_user.id} '
                                                   f'by @{message.from_user.username} was successful')
    await asyncio.sleep(10)
    await start_message(message, state)


def register_handlers_client(dp: Dispatcher):
    dp.message.register(start_message, commands=['start'])
    dp.callback_query.register(start_callback, text='back_2_menu', state=Funnel.serial_buy)
    dp.callback_query.register(serial_buy, text='serials_buy', state=Funnel.main_change)
    dp.callback_query.register(get_feedback, text='leave_feedback', state=Funnel.main_change)
    dp.callback_query.register(main_menu_navigate, state=Funnel.main_change)
    dp.message.register(save_feedback, state=Funnel.get_feedback)
    dp.pre_checkout_query.register(serial_pre_buy_checkout_query, state=Funnel.serial_buy)
    dp.message.register(serial_successful_payment, content_types=[ContentType.SUCCESSFUL_PAYMENT],
                        state=Funnel.serial_buy)
