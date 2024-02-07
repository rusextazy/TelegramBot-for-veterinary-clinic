from aiogram.fsm.state import State, StatesGroup


class Reception(StatesGroup):
    Info_Client = State()
    Info_Animal = State()
    Info_Doc = State()
