from aiogram import html
from aiogram.utils.markdown import hide_link


start_text: str = (
            html.bold("Здарова, cyberпреступник! 🥶\n")
            + html.bold("С помощью бота ты сможешь обойти санкции тиктока против России.\n\n")
            + html.italic("Чтобы все заработало, "
                          "сначала установи необходимый файл с модом, нажав по кнопке «Файл»\n\n")
            + html.italic("После установки нажми на «Видеоинструкция» для просмотра инструкций по настройки мода\n\n")
            + html.bold("Если все сработало - поздравляю,"
                        " теперь ты можешь спокойно смотреть свежие видео в тикток!👊🏼\n")
            + html.bold("Если же нет- попробуй пересмотреть инструкцию, и убедись, что все сделал правильно.\n\n")
            + f"На случай если остались вопросы - @yeyo81"
    )


feedback_text: str = (
    f"{hide_link('https://i.imgur.com/miWCDDk.png')}"
    f"Спасибо за отзыв!"
)
