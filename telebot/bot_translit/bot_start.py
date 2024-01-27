from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

star = Router()


@star.message(CommandStart())
async def start(massage: Message):
    await massage.answer(text=f"Привет {massage.from_user.full_name}")
