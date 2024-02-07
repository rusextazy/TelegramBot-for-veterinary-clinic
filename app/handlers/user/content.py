from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.keyboards.reply import kb_menu, kb_menu_product
from app.text.main import pet_supplies_text, contacts_text
from app.text.price import price_text


router = Router()


@router.message(F.text == "🔙 Главное меню")
@router.message(F.text == "Отмена")
@router.message(F.text == "Меню")
async def main_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.reply(text="Вы вернулись на главное меню!", reply_markup=kb_menu)


@router.message(F.text == "📌 Зоотовары")
async def replenish(msg: Message):
    await msg.answer(text=pet_supplies_text, reply_markup=kb_menu_product)


@router.message(F.text == "📞 Контакты")
async def replenish(msg: Message):
    await msg.answer(text=contacts_text)


@router.message(F.text == "💰 Price")
async def replenish(msg: Message):
    await msg.answer(text=price_text)
