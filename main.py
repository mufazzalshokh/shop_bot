# import telebot
#
# bot = telebot.TeleBot('1761629215:AAHaNz02RBrxHB2YCyOvr-LPh1GfhwlkrY4')
#
#
# @bot.message_handler(func=lambda x: True)
# def send_welcome(message):
#     x = message.text.split(' ')
#     a = int(x[0])
#     b = x[1]
#     c = int(x[2])
#
#     if b == '+':
#         g = a + c
#     elif b == '-':
#         g = a - c
#     elif b == '*':
#         g = a * c
#     else:
#         g = a / c
#
#     bot.send_message(message.chat.id, g)
#
#
# bot.polling()
