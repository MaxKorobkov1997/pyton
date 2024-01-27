from aiogram import Router

from aiogram.types import Message

from keybord import Links
import globals

hendlers = Router()
a = ''
b = ''


@hendlers.message()
async def otv(massage: Message):
    global a, b
    a = massage.chat.id
    b = massage.text
    if massage.text:
        await massage.answer(text='на какой язык перевести',
                             reply_markup=Links)
    else:
        await massage.answer(text=f"Отправьте текст")


def vheb():
    globals.save = a
    globals.text = b
