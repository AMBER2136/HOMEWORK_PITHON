# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN
# N может быть любой длины.
# N = 132:
# 132 + 132132 + 132132132 = 132264396
real = str(input('Введите натуральное число '))
real_1 = real + real
real_2 = real*3
result = int(real) + int(real_1) + int(real_2)
print(f'Результат: {result}')