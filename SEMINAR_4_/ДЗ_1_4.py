# Задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

num = 999136
real = 2
for j in range(1, num+1, 1):
    while(num > 1):
        rem = num%real
        if(rem == 0):
            num = num/real
            print(real)
        else:
            real +=1