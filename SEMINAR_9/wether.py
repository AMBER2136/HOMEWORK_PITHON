import telebot
import requests

bot = telebot.TeleBot("5634103797:AAFOLvXdoQGU8a2U-OWsO6OFo9BENYxr-3s", parse_mode=None)

   
@bot.message_handler(commands = ['OOO'])
def play_guess(message):
    bot.reply_to(message, 'УРА! УРА! УРА!')

@bot.message_handler(content_types = ['text'])
def react_message(message):
    if message.text == 'TTT':
        bot.reply_to(message, 'BBBBBBB')
    elif message.text == 'погода':
        ddd = requests.get('https://wttr.in/Vologda?format=3') # Вариант отображения погоды 1.
        bot.reply_to(message, ddd.text)
    else:
        print(f'От {message.from_user.first_name} {message.from_user.last_name} сообщение: {message.text}')
        bot.reply_to(message, message.text)

@bot.message_handler(content_types = ['text'])
def react_message(message):
    if message.text == 'DDD':
        bot.reply_to(message, 'BBBBBBB')
    elif message.text == 'погода':
        ddd = requests.get('https://wttr.in/Vologda?0T') # Вариант отображения погоды 2.
        bot.reply_to(message, ddd.text)
    else:
        print(f'От {message.from_user.first_name} {message.from_user.last_name} сообщение: {message.text}')





        bot.reply_to(message, message.text)


    




bot.infinity_polling()