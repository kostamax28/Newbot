from aiogram import Bot, types

from aiogram.dispatcher import Dispatcher

from aiogram.utils import executor

TOKEN = "5446519593:AAHWfTBE-YJeKbJFT6l9WXROPxp87vR9mWk"

bot = Bot(token=TOKEN)



dp = Dispatcher(bot)
dp.message_handler(commands=['start', 'help'])

async def send_welcome(msg: types.Message):

    await msg.reply_to_message(‘Я бот. Приятно познакомиться,

                               {msg.from_user.first_name}’)
@dp.message_handler(content_types=['text'])

async def get_text_messages(msg: types.Message):

   if msg.text.lower() == 'привет':

       await msg.answer('Привет!')

   else:

       await msg.answer('Не понимаю, что это значит.')   
if __name__ == '__main__':

   executor.start_polling(dp)       
