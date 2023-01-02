# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
num = float(input('Введите целое число больше 0  '))
if num > 0 and num % 1 == 0:
    num = int(num)
    list_num = list(range(1,num+1,1))
    fact = 1
    for i in list_num:
        fact = fact*list_num[i-1]
        print(fact)
if num < 1: 
    print('Введено 0 или отрицательное число')
if num % 1 != 0:
    print('Введено не целое число')



