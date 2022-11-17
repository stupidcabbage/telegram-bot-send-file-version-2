import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from config_reader import config
from handlers import questions, feedback

CHAT_ID_ADMIN = config.chat_id_admin.get_secret_value()

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(
        token=config.bot_token.get_secret_value(),
        parse_mode="HTML"
    )
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(questions.router)
    dp.include_router(feedback.router)

    await bot.send_message(chat_id=CHAT_ID_ADMIN, text="Бот включен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
