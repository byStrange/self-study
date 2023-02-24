import logging
from db import vote, most_voted

from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '5084415268:AAF07r-9pYvTtQJZ086BOr2r5iZxb8dG5q4'

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Hi I'm vote bot powered by myself")
    await message.reply("📢 You can vote one of these countries. Don't worry this bot is only for testing 😉")
    keyboard = types.ReplyKeyboardMarkup()
    buttons = ['Ukraine', 'America', 'Russia']
    keyboard.add(*buttons)
    await message.answer("CHOOSE :)", reply_markup=keyboard)
    
@dp.message_handler(lambda message: message.text == "Ukraine")
async def with_puree(message: types.Message):
    vote('ukraine', f"{message['from']['id']}")
    await message.reply("Thanks for voting")

@dp.message_handler(lambda message: message.text == "America")
async def with_puree(message: types.Message):
    vote('America', f"{message['from']['id']}")
    await message.reply("Thanks for voting")

@dp.message_handler(lambda message: message.text == "Russia")
async def with_puree(message: types.Message):
    vote('Russia', f"{message['from']['id']}")
    await message.reply("Thanks for voting")


@dp.message_handler(commands=['show'])
async def show(message: types.Message):
    most = most_voted()
    await message.reply(f"""
        Most voted coutry: {most['most'][0]} voted 📢 {most['most'][1]} times
        Others countries:
        America {most['all']['en']}
        Russia {most['all']['ru']}
        Ukraine {most['all']['uk']}
    """)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)