import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

# Объект бота
bot = Bot(token='5573444471:AAHqxNHgjaLe-tMUz6mPRdqlqmp-H4SbJOQ')
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Диспетчер для бота
dp = Dispatcher(bot)


# Кнопки
@dp.message_handler(commands="go")
async def push_button(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Кнопка 1")
    button_2 = types.KeyboardButton(text="Кнопка 2")
    keyboard.add(button_1, button_2)
    await message.answer("Какую кнопку выберешь ТЫ?", reply_markup=keyboard)


# Ответы при нажатии на кнопки
@dp.message_handler(Text(equals="Кнопка 1"))
async def with_button_one(message: types.Message):
    await message.reply("Отлично, ты первый!")


@dp.message_handler(lambda message: message.text == "Кнопка 2")
async def with_button_two(message: types.Message):
    await message.reply("Ничего, ты второй")


# Дублирование сообщения
@dp.message_handler()
async def bot_answer(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
