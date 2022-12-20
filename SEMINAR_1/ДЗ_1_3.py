a=int(input('Введите номер квадранта   '))
print(a)
if (a < 1) or (a > 4):
    print('Ошибка ввода, квадрантов четыре.')
if a == 1:
    print('x>0; y>0')
if a == 2:
    print('x<0; y>0')
if a == 3:
    print('x<0; y<0')
if a == 4:
    print('x>0; y<0')
