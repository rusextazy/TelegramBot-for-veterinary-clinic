from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

kb_greeting = [
    [InlineKeyboardButton(text="Директор", url="https://t.me/spectropfobia"),
     InlineKeyboardButton(text="Создатель", url="https://t.me/rusextaz")],
    [InlineKeyboardButton(text="Канал", url="https://t.me/rusextazHub")]
]

kb_greeting = types.InlineKeyboardMarkup(inline_keyboard=kb_greeting)


class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int


def paginator(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="➡️", callback_data=Pagination(action="next", page=page).pack()),
        width=2
    )
    return builder.as_markup()


adms = [
    [InlineKeyboardButton(text="Принять", callback_data="yes"),
     InlineKeyboardButton(text="Отклонить", callback_data="no")]
]

adms = types.InlineKeyboardMarkup(inline_keyboard=adms)