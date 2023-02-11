import telebot

def answer_to_client(id, question, answer):
    bot.send_message(id, f'{question} \n{answer}')

bot = telebot.TeleBot("5634103797:AAFOLvXdoQGU8a2U-OWsO6OFo9BENYxr-3s", parse_mode=None)

with open('request.txt', 'r', encoding = 'utf-8') as stream:
    request_list = stream.readlines()
    
    closed_requests = []
    for line in request_list:
        pos_line = line.split('#')
        question = pos_line[0]
        name = pos_line[1]
        id = pos_line[2]
        date_time = pos_line[3]
        print(f'{name} {question} {date_time}')
        answer = input('Введите ответ ')
    
        if answer != 'не стоит напрягаться':
            answer_to_client(id, question, answer)
            closed_requests.append(line)
        print('++++++++++++++++++++++++++++++++++++++')

    for i in closed_requests:
        request_list.remove(i)
    with open('request.txt', 'w', encoding = 'utf-8') as stream:
        stream.writelines(request_list) 
        




bot.infinity_polling()