from aiogram import Router, Bot
from vois_chat import chat_vosi
from aiogram.types.input_file import FSInputFile
import config
from translitir import translate_text
from hendlers import vheb
import globals
import os

calbak = Router()
bot = Bot(token=config.BOT_TOKEN)


@calbak.callback_query()
async def calback(callback):
    globals.incilizatjr()
    vheb()
    print(f'{globals.save} нтиемскучв {globals.text}')
    audio_save = f'{globals.save}.mp3'
    translation = translate_text(globals.text, callback.data)
    chat_vosi(globals.text, audio_save)
    otk = FSInputFile(path=audio_save)
    await bot.send_message(chat_id=callback.from_user.id,
                           text=translation)
    await bot.send_voice(chat_id=callback.from_user.id,
                         voice=otk)
    await callback.answer()
    os.remove(audio_save)
