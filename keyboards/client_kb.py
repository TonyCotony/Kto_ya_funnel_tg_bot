from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

client_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Знакомство',
            callback_query='client_meet'
        )
    ],
    [
        InlineKeyboardButton(
            text='Музыкальная атмосфера',
            callback_query='client_music_atmo'
        )
    ],
    [
        InlineKeyboardButton(
            text='Книга KtoYa',
            callback_query='client_book'
        )
    ],
    [
        InlineKeyboardButton(
            text='Сериал "Активация Гениальности"',
            callback_query='client_serial'
        )
    ],
    [
        InlineKeyboardButton(
            text='Отзывы',
            callback_query='client_feedback'
        ),

        InlineKeyboardButton(
            text='Связь со мной',
            callback_query='client_my_contacts'
        )
    ],
    [
        InlineKeyboardButton(
            text='Подкасты "Созерцай"',
            callback_query='client_podcasts'
        )
    ]
])

client_back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='<<<Назад',
            callback_data='back_2_menu'
        )
    ]
])

client_back_n_feedback_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Оставить отзыв',
            callback_data='leave_feedback'
        )
    ],
    [
        InlineKeyboardButton(
            text='<<<Назад',
            callback_data='back_2_menu'
        )
    ]
])

serials_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Хочу продолжение!!!',
            callback_data='serials_buy'
        )
    ],
    [
        InlineKeyboardButton(
            text='<<<Назад',
            callback_data='back_2_menu'
        )
    ]
])

podcasts_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Тени и Дары',
            callback_data='shadows'
        )
    ],
    [
        InlineKeyboardButton(
            text='Сиддхи',
            callback_data='siddhi'
        )
    ],
    [
        InlineKeyboardButton(
            text='<<<Назад',
            callback_data='back_2_menu'
        )
    ]
])

siddhi_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Подробнее о Сиддхи',
            callback_data='buy_siddhi'
        )
    ],
    [
        InlineKeyboardButton(
            text='О подкасте Тени и Дары',
            callback_data='shadows'
        )
    ],
    [
        InlineKeyboardButton(
            text='<<<Назад',
            callback_data='back_2_menu'
        )
    ]
])

shadows_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Подробнее о Тенях и дарах',
            callback_data='buy_shadows'
        )
    ],
    [
        InlineKeyboardButton(
            text='О подкасте Тени и Дары',
            callback_data='siddhi'
        )
    ],
    [
        InlineKeyboardButton(
            text='<<<Назад',
            callback_data='back_2_menu'
        )
    ]
])
