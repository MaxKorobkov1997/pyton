from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='english', callback_data='en')
        ],
        [
            InlineKeyboardButton(text='russian', callback_data='ru')
        ],
        [
            InlineKeyboardButton(text='belarusian', callback_data='be')
        ]
    ]
)
