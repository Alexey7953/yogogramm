import config
import logging
from aiogram import Bot, Dispatcher, executor

logging.basicConfig(Level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: type.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
