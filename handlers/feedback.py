from aiogram import Router, types
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import StatesGroup, State
from aiogram.methods.forward_message import ForwardMessage
from config_reader import config
from .for_questions import come_back

CHAT_ID_ADMIN = config.chat_id_admin.get_secret_value()

router = Router()


class FeedBack(StatesGroup):
    write_feedback = State()


@router.message(lambda message: message.text == "Оставить отзыв")
async def feedback(message: types.Message, state: FSMContext):
    await message.answer('Отправь все одним сообщением ниже')
    await state.set_state(FeedBack.write_feedback)


@router.message(FeedBack.write_feedback)
async def reply_feedback(message: types.Message, state: FSMContext):
    await state.update_data(feedback=message)
    await message.answer(
        text="Спасибо за отзыв!",
        reply_markup=come_back()
    )
    await ForwardMessage(from_chat_id=message.chat.id, chat_id=CHAT_ID_ADMIN, message_id=message.message_id)
    await state.clear()
