day_name = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
'Пятница', 'Суббота', 'Воскресенье']
a=float(input('Введите целое число от 1 до 7 включительно  '))
if a>=1 and a<=7 and a%1==0:       
    a=int(a)
    print(day_name[a-1])
if (a % 1) !=0:
    print('Введено не целое число')
if a>7 or a<1: 
    print('Введено число за пределами числового отрезка')

