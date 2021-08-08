# import telebot
#
# bot = telebot.TeleBot('1761629215:AAHaNz02RBrxHB2YCyOvr-LPh1GfhwlkrY4')
#
# users = dict()
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, 'Salom, ismingizni kiriting')
#
#     bot.register_next_step_handler(message, get_name)
#
#
# def get_name(message):
#     users[message.from_user.id] = dict()
#     users[message.from_user.id]['name'] = message.text
#
#     bot.send_message(message.chat.id, 'Yoshingizni kiriting')
#
#
# def get_age(message):
#     users[message.from_user.id]['age'] = message.text
#
#     text = f'Ismingiz: {users[message.from_user.id]["name"]}\nYoshingiz{users[message.from_user.id]["age"]}'
#
#     bot.send_message(message.chat.id, text)
#
#
# bot.polling()
