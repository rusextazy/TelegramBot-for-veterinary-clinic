from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import types

from app.utils.state import Reception
from app.text.doctors import odobreno_zapis, otkloneno_zapis, reception_zai, zapis_priem
from app.keyboards.reply import kb_exit, kb_menu
from app.keyboards.inline import adms

router = Router()


@router.callback_query(F.data.in_(('yes', 'no')))
async def process_callback(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'yes':
        await bot.send_message(chat_id=id_message, text="✅")
        await bot.send_message(chat_id=id_message,
                               text="Ваша запись на прием одобрена! Подробнее у @spectropfobia")
        await bot.send_message(chat_id='-4086537550',
                               text=odobreno_zapis.format(id=id_message,
                                                          name=chel_message,
                                                          user=user_message))
    elif callback.data == 'no':
        await bot.send_message(chat_id=id_message, text="❌")
        await bot.send_message(chat_id=id_message,
                               text="Ваша запись на прием отклонена! Подробнее у @spectropfobia")
        await bot.send_message(chat_id='-4086537550',
                               text=otkloneno_zapis.format(id=id_message,
                                                           name=chel_message,
                                                           user=user_message))
    await callback.message.delete_reply_markup()
    await callback.answer()


@router.message(F.text == "📈 Записать на прием")
async def reception(msg: Message, state: FSMContext):
    await state.update_data()
    await msg.answer(text="Для записи на прием проследуйте дальнейшей инструкции ⬇️\n")
    await msg.answer(text="Введите ваши данные: \nФИО, номер телефона\n(ПРИМЕР: Иванов Иван Иванович, 89518594631)",
                     reply_markup=kb_exit)
    await state.set_state(Reception.Info_Client)


@router.message(Reception.Info_Client)
async def get_name_info(msg: Message, state: FSMContext):
    await state.update_data(client_info=msg.text)
    info_client = await state.get_data()
    print(info_client['client_info'])
    await msg.answer(text="Вид, порода и кличка Вашего питомца\n(ПРИМЕР: собака, доберман, Зая)")
    await state.set_state(Reception.Info_Animal)


@router.message(Reception.Info_Animal)
async def get_animal_info(msg: Message, state: FSMContext):
    await state.update_data(animal_info=msg.text)
    info_client_animal = await state.get_data()
    print(info_client_animal['animal_info'])
    await msg.answer(text="Введите фамилию врача и желаемую дату посещения\n(ПРИМЕР: Минеева, 29.09.23)")
    await state.set_state(Reception.Info_Doc)


@router.message(Reception.Info_Doc)
async def get_doc_info(msg: Message, bot: Bot, state: FSMContext):
    await state.update_data(doc_info=msg.text)
    info_client = await state.get_data()
    info_client_animal = await state.get_data()
    info_doc = await state.get_data()
    print(info_doc['doc_info'])
    await msg.answer(
        zapis_priem.format(fio=info_client['client_info'], animal=info_client_animal['animal_info'],
                           doktor=info_doc['doc_info']))
    await msg.answer(text="❤️", reply_markup=kb_menu)
    await bot.send_message(chat_id='-4086537550',
                           text=reception_zai.format(id=msg.from_user.id,
                                                     name=msg.from_user.full_name,
                                                     user=msg.from_user.username,
                                                     fio=info_client['client_info'],
                                                     animal=info_client_animal['animal_info'],
                                                     doktor=info_doc['doc_info']),
                           reply_markup=adms)
    global id_message
    id_message = msg.chat.id
    global chel_message
    chel_message = msg.from_user.full_name
    global user_message
    user_message = msg.from_user.username
    await state.clear()
