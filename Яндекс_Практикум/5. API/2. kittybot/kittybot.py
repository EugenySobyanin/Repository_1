from telebot import TeleBot

TOKEN = '7429904478:AAEwhh25SYpvnqC2Ripelbn6Rl_E0u8HEGc'
MY_CHAT_ID = '5622194552'

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def lets_go(message):
    bot.send_message(chat_id=message.chat.id, text="Пошел отсюда.")


@bot.message_handler(content_types=['text'])
def say_hai(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text="Всем привет меня зовут!")


bot.polling()
