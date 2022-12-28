import telebot
bot = telebot.TeleBot('5805282132:AAF6oeYx5cfCGkbnO4nV4qluAG4L0YIVRnQ')
bot.set_webhook()

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode='html')



bot.polling(none_stop=True)
