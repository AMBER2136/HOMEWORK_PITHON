# Задача 3. Создайте скрипт бота, который находит 
# ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

def load_file_dictionary():
    stream = open('bot.txt', mode = 'r', encoding='utf-8')
    suffix_phrase_list = stream.readlines()
    stream.close()
    dictionary = {}
    for phrase in suffix_phrase_list:
        phrase = phrase.removesuffix('\n')
        phrase = phrase.split(': ')
        dictionary[phrase[0]] = phrase[1]
    return dictionary
bot_dictionary = load_file_dictionary()

in_dialog = True
while in_dialog:
    sentence = input('Наташа:')
    sentence = sentence.lower()
    if sentence in bot_dictionary.keys():
        print(f'Бот:{bot_dictionary[sentence]}')
    if sentence == 'до свидания':
        in_dialog = False
    if (sentence in bot_dictionary.keys()) == False:
        print('Бот: Я не понимаю, что Вы сказали.')
        ask = input('Бот: Хотите научить меня правильному ответу(Да/Нет)?\nНаташа:')
        ask = ask.lower()
        if ask == 'да':
            answer = input(f'Как бы ты ответила на фразу "{sentence}"?\nНаташа:')
            str_eam = open('bot.txt', mode = 'a', encoding='utf-8')
            str_eam.write(f'{sentence}: {answer}\n')
            str_eam.close()
            bot_dictionary[sentence] = answer
        


