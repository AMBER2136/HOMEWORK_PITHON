import random

secret_number = random.randint(0, 30)
print(secret_number)
player_number = int(input('Попробуйте угадать число. '  
                        'Введите целое число от 1 до 30  '))
count = 0
while player_number != secret_number:
    print('Вы не угадали')
    count += 1
    if secret_number > player_number + 4:
        print('Это число больше, чем Ваше плюс 4')
    if secret_number < player_number + 4:
        print('Это число меньше, чем Ваше плюс 4')
    if secret_number > player_number - 2 :
        print('Это число больше, чем Ваше минус 2')
    if secret_number < player_number - 2 :
        print('Это число меньше, чем Ваше минус 2')
    player_number = int(input('Попробуйте еще раз. '  
                        'Введите целое число от 1 до 30  '))
    if player_number == secret_number:
        print(f'Вы угадали, это число {secret_number}')
        print(f'Было {count} неудачных попыток.')
    
