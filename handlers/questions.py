from aiogram import Router, types
from aiogram.utils.markdown import hlink
from .for_questions import start_answer, back_and_feedback, come_back
from .feedback import feedback_chat
from .BASE_FILE_ID import TIK_TOK_LIA
from .texts import start_text

router = Router()


@router.message(commands=["start"])
async def cmd_start(message: types.Message):
    builder = feedback_chat()
    await message.answer(
        start_text,
        reply_markup=start_answer()
    )
    await message.answer(
        "Ознакомиться с отзывами можно по ссылке ниже",
        reply_markup=builder.as_markup()
    )


@router.message(lambda message: message.text == "Получить файл!💍")
async def answer_file(message: types.Message):
    file_id: str = TIK_TOK_LIA
    await message.reply_document(file_id, reply_markup=back_and_feedback())
    await message.answer("Если тебе все понравилось - ты можешь оставить отзыв, нам будет приятно 🗣")


@router.message(lambda message: message.text == "Видеоинструкция")
async def answer_video(message: types.Message):
    await message.reply("Ознакомиться с инструкцией можно перейдя по ссылке ниже.👇")
    await message.reply(
        hlink("Сама инструкция", 'https://www.youtube.com/watch?v=RI9fDipxj4o&t=120s'),
        reply_markup=come_back()
    )


@router.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message):
    await message.answer(
        start_text,
        reply_markup=start_answer()
    )
