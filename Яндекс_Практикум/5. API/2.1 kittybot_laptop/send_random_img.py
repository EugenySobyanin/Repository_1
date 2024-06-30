# kittybot/send_random_image.py
import requests
from telebot import TeleBot


bot = TeleBot(token='7429904478:AAEwhh25SYpvnqC2Ripelbn6Rl_E0u8HEGc')

URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
random_cat_url = response[0].get('url')


chat_id = '5622194552'

# Отправка изображения
bot.send_photo(chat_id, random_cat_url)