from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from core.keybuttons.keyboard_buttons import search_button

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        text="Для работы с ботом вам нужно будет ввести год.",
        reply_markup=search_button,
    )
