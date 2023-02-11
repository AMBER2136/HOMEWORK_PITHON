import telebot
from datetime import datetime as dt
# import requests

bot = telebot.TeleBot("5634103797:AAFOLvXdoQGU8a2U-OWsO6OFo9BENYxr-3s", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте, я бот техподдержки. Опишите Вашу проблему.")
    bot.register_next_step_handler(message, record_question)
def record_question(message):
    with open('request.txt', 'a', encoding = 'utf-8') as stream:
        stream.write(f'"{message.text}"# От: {message.from_user.first_name} \
{message.from_user.last_name}  #{message.from_user.id}# \
Date/Time: {dt.fromtimestamp(message.date)}\n')
    bot.reply_to(message, 'Ваше сообщение принято и передано оператору. \
Ожидайте. Ответ непременно воспоследует.')    
    print(message)
    print(dt.fromtimestamp(message.date))

@bot.message_handler(commands = ['log_report'])
def log_file_report(message):    
    with open('log_file.txt', 'r', encoding = 'utf-8') as stream:
        report = stream.read()
        print(report)
    bot.reply_to(message, report)

# @bot.message_handler(content_types=['text'])
# def log_file(message):
#     with open('log_file.txt', 'a', encoding = 'utf-8') as stream:
#         stream.write(f'"{message.text}" От {message.from_user.first_name} {message.from_user.last_name} {message.from_user.id} {dt.fromtimestamp(message.date)}\n')
#     print(message)
#     print(dt.fromtimestamp(message.date))



bot.infinity_polling()