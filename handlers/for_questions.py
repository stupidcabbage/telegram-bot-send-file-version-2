from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_answer() -> ReplyKeyboardMarkup:
    """Кнопки, создающие ссылки видеоинструкции и получения файла"""
    kb = [
        [
            KeyboardButton(text="Видеоинструкция"),
            KeyboardButton(text="Получить файл!💍")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите необходимый пункт, приведенный ниже.",
        one_time_keyboard=True
    )
    return keyboard


def back_and_feedback() -> ReplyKeyboardMarkup:
    kb = [
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Оставить отзыв")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите необходимый пункт, приведенный ниже."
    )
    return keyboard


def come_back() -> ReplyKeyboardMarkup:
    kb = [
        [
        KeyboardButton(text="Назад")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Возвращаемся назад?"
    )
    return keyboard
