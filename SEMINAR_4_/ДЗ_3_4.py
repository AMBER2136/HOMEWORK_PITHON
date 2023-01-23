#  Задача 3. Выведите число π с заданной точностью. 
# Точность выводится в виде десятичной дроби.
# 0.001 -> 3.142
import math
acc = 0.00001
inv_acc = int(math.log10(1 / acc))
pi = round(2*math.acos(0.0),inv_acc)
print(f'{acc} => {pi}')


