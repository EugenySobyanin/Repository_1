
import logging
import os
import requests

from dotenv import load_dotenv
from telebot import TeleBot, types

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv('TOKEN')
URL_CAT = os.getenv('URL_CAT')
URL_DOG = os.getenv('URL_DOG')
# MY_CHAT_ID = '5622194552'

bot = TeleBot(token=TOKEN)


def get_new_image():
    try:
        response = requests.get(URL_CAT)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = URL_DOG
        response = requests.get(new_url)

    return response.json()[0].get('url')


@bot.message_handler(commands=['newcat'])
def new_cat(message):
    chat = message.chat
    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(commands=['start'])
def lets_go(message):
    chat = message.chat
    name = chat.first_name
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('/newcat')
    keyboard.add(button)
    bot.send_message(
        chat_id=message.chat.id, 
        text=f"Пошел отсюда, {name}.",
        reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def say_hai(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text="Всем привет меня зовут Олег!")


def main():
    bot.polling()


if __name__ == '__main__':
    main()
