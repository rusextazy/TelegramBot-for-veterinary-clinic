from aiogram import Router, F
from aiogram.types import Message

from app.text.main import pet_pharmacy_text, pet_supplies_text
from app.text.pet_supplies import dog_text, cat_text, rodents_text, pharmacy_text

router = Router()


@router.message(F.text == "🦮 Товары для собак")
async def replenish(msg: Message):
    await msg.answer(text=dog_text)


@router.message(F.text == "🐈 Товары для кошек")
async def replenish(msg: Message):
    await msg.answer(text=cat_text)


@router.message(F.text == "🐹 Товары для грызунов")
async def replenish(msg: Message):
    await msg.answer(text=rodents_text)


@router.message(F.text == "🧬 Аптека")
async def replenish(msg: Message):
    await msg.answer(text=pet_pharmacy_text)
    await msg.answer(text=pharmacy_text)
