from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_menu = [
    [KeyboardButton(text="💊 Врачи"),
     KeyboardButton(text="💰 Price")],
    [KeyboardButton(text="📞 Контакты"),
     KeyboardButton(text="📌 Зоотовары")],
    [KeyboardButton(text="📈 Записать на прием")]
]

kb_menu = ReplyKeyboardMarkup(keyboard=kb_menu, resize_keyboard=True)

kb_menu_product = [
    [KeyboardButton(text="🐈 Товары для кошек"),
     KeyboardButton(text="🦮 Товары для собак")],
    [KeyboardButton(text="🐹 Товары для грызунов"),
     KeyboardButton(text="🧬 Аптека")],
    [KeyboardButton(text="🔙 Главное меню")]
]

kb_menu_product = ReplyKeyboardMarkup(keyboard=kb_menu_product, resize_keyboard=True)

kb_exit = [
    [KeyboardButton(text="🔙 Главное меню")]
]

kb_exit = ReplyKeyboardMarkup(keyboard=kb_exit, resize_keyboard=True)