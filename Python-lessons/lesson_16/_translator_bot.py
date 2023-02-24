import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(message.chat.id, f"Hello {message.from.first_name}")

@bot.message_handler(content_types=['text'])
def all(m):
    translated = translator.translate(m.text, dest="en", src="uz")
    bot.send_message(message.chat.id, translated.text)

bot.infinity_polling()