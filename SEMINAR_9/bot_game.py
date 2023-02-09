import telebot
import random
from telebot import types

game_on = False
secret_number = None

bot = telebot.TeleBot("5634103797:AAFOLvXdoQGU8a2U-OWsO6OFo9BENYxr-3s", parse_mode=None)
# comand_list = ['/play_guess', '/stop']

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Хочу играть')
itembtn2 = types.KeyboardButton('Хочу считать')
markup.add(itembtn1, itembtn2)

def calculate(message):
    bot.reply_to(message, f'Ответ = {eval(message.text)}')      
   
@bot.message_handler(commands = ['help'])
def play_guess(message):
    bot.reply_to(message, 'Хотите играть? Напишите "Хочу играть". \
                           Хотите считать? Напишите "Хочу считать"', reply_markup = markup)    
 

@bot.message_handler()
def react_message(message):
    global secret_number
    global game_on
   
    if game_on:
        if message.text.isdigit():
            player_number = int(message.text)
            if player_number == secret_number:
                game_on = False
                bot.reply_to(message, f'Вы угадали, это число {secret_number}')
                
            elif secret_number > player_number + 4:
                bot.reply_to(message, 'Это число больше, чем Ваше плюс 4')
            elif secret_number < player_number + 4:
                bot.reply_to(message,'Это число меньше, чем Ваше плюс 4')
            else:
                bot.reply_to(message, 'Попробуйте еще раз')
        else: 
            bot.reply_to(message, 'Надо непременно ввести именно число')
            return
    elif message.text == 'Привет':
        bot.reply_to(message, 'Хотите играть? Напишите "Хочу играть". \
Хотите считать? Напишите "Хочу считать"', reply_markup = markup)
    elif message.text == 'Хочу играть':
        if not game_on:
            game_on = True
            secret_number = random.randint(0, 30)
            print(secret_number)
            bot.reply_to(message, 'Я задумал число от 1 до 30. Попробуйте угадать его. А я помогу. \
Смелее вводите число')
        else:
            bot.reply_to(message, 'Вы уже играете, введите число')   
    elif message.text == 'Хочу считать':
        bot.reply_to(message, 'Введите выражение')
        bot.register_next_step_handler(message, calculate)         
    else:
        bot.reply_to(message, 'Поздоровайтесь со мной, введите "Привет"')   

bot.infinity_polling()