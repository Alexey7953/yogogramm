import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler
async def pb():
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Кнопка 1")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Кнопка 2")
    keyboard.add(button_2)


@dp.message_handler()
async def bot_answer(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
