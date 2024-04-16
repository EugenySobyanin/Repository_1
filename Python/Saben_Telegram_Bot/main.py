import telebot
import webbrowser

bot = telebot.TeleBot('6729216549:AAFZqaY8kTsR_Jm4VH6MBqed0e6yLjz-9MM')


# обрабатывает команды

# обычная команда
@bot.message_handler(commands=['start', 'main',])
def main(message):
    bot.send_message(message.chat.id, '<b>Привет, нинидзя!</b>', parse_mode='html')

# берет информацию из объекта message
@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, 
                     f'<b>Привет, {message.from_user.last_name}!</b>', parse_mode='html')

# выводит объект message полностью
@bot.message_handler(commands='info')
def info(message):
    bot.send_message(message.chat.id, message)

# делает переход на веб страницу
@bot.message_handler(commands=['site', 'website'] )
def site(message):
    webbrowser.open('https://ya.ru/')







# обробатывает сообщения
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Здарова, братишка!', parse_mode='html')




bot.polling(non_stop=True)
