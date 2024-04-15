from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.types.states import SearchState
from core.keybuttons.keyboard_buttons import cancel_button

router = Router()


@router.message(Command("search"))
async def search(message: Message, state: FSMContext):
    await state.set_state(SearchState.search)
    await message.answer(
        text="Для поиска возможных абитуриентов в <u>(Крым, Севастополь)</u> по году окончания школы, <i><b>введите год окончания школы</b></i>:",
        parse_mode="HTML",
    )


@router.message(Command("cancel"), F.text == "/cancel", SearchState.search)
async def cancel(message: Message, state: FSMContext):
    await message.answer(text="Вы отменили поиск студентов", reply_markup=cancel_button)
    await state.clear()


@router.message(F.text)
async def input_year_of_school(message: Message, state: FSMContext):
    response = message.text.strip()
    if response.isdigit() and len(response) == 4:
        await state.set_state(SearchState.run)
        await message.answer(
            text="<b>Поиск запущен, ожидайте!</b>\n\n<i>Обычно занимает от x до y</i>",
            parse_mode="HTML",
        )
    """Вообщем сдесь и возникают проблемы, нужно чтобы ты метод get_schools посмотрел, он не выводит значения, на данный момент времени.
    Если ты его сделаешь, то дай мне дописать бота. Плюс там в методах есть небольшие косяки в папке types и mixin там просто написанно 
    Country почти во всех методах from_dict
    
    """
