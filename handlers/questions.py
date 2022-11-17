from aiogram import Router, types
from aiogram.utils.markdown import hlink
from .for_questions import start_answer, back_and_feedback, come_back
from .BASE_FILE_ID import TIK_TOK_LIA
from .texts import start_text

router = Router()


@router.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        start_text,
        reply_markup=start_answer()
    )


@router.message(lambda message: message.text == "Получить файл!💍")
async def answer_file(message: types.Message):
    file_id: str = TIK_TOK_LIA
    await message.reply_document(file_id, reply_markup=back_and_feedback())


@router.message(lambda message: message.text == "Видеоинструкция")
async def answer_video(message: types.Message):
    await message.reply("Ознакомиться с инструкцией можно перейдя по ссылке ниже.👇")
    await message.reply(
        hlink('Сама инструкция', 'https://www.youtube.com/watch?v=RI9fDipxj4o&t=120s'),
        reply_markup=come_back()
    )


@router.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message):
    await message.answer(
        start_text,
        reply_markup=start_answer()
    )
