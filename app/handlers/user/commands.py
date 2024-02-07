from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.markdown import hide_link

from app.text.main import greeting_text
from app.keyboards.inline import kb_greeting
from app.keyboards.reply import kb_menu


router = Router()


@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer(greeting_text.format(name=msg.from_user.full_name,
                     link=f"{hide_link('https://i.ytimg.com/vi/nh0g83A7PKQ/maxresdefault.jpg')}"),
                     reply_markup=kb_greeting)
    await msg.answer_sticker("CAACAgIAAxkBAAEBMmxlEbAmqpMTyGFsnzdlfpA67p1DLAACiysAApunuUpnYzvhbe6O7zAE", reply_markup=kb_menu)