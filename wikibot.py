import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6769675725:AAElHkCaQHKu_VbklXCdVi7IebMICjoxdBA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom Wikipedia Botimizga Xush Kelibsiz!")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)