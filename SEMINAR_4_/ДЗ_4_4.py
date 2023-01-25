# Задача 4*. Даны два файла, в каждом из которых находится 
# запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8
stream = open('polynom_1.txt', mode ='r', encoding='utf-8')
polynom_1 = stream.read()
stream.close()
print(polynom_1)
stream = open('polynom_2.txt', mode ='r', encoding='utf-8')
polynom_2 = stream.read()
stream.close()
print(polynom_2)
lenth_1 = len(polynom_1)
lenth_2 = len(polynom_2)
for j in polynom_1:
    print(j, end=', ')
poly_list = polynom_1.split('X^2')
print(poly_list)

poly_list_1 = poly_list[1].split('X')
print(poly_list_1)
