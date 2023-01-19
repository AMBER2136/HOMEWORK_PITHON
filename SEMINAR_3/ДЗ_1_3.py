# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
def fibon(z):
    fibo_1, fibo_2= 0, 1
    print(fibo_1)
    file = open('fibon.txt', mode = 'w',encoding = 'utf-8')
    file.writelines(str(fibo_1) + '\n')
    for _ in range(1,z,1):
        fibo_1, fibo_2 =fibo_2, fibo_1 + fibo_2  
        print(fibo_1)        
        file.writelines(str(fibo_1) + '\n')
    file.close
num = int(input('Введите целое положительное число   '))
fibon(num)
file = open('fibon.txt', mode = 'r',encoding = 'utf-8')
print(file)
file_content = file.read()
print(file_content)
file.close

