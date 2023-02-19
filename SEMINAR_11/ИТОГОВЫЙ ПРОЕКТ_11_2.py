# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список 
# подходящих ему домов,
# отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import numpy as npy
import matplotlib.pyplot as plt

size = 15
hous = npy.random.randint(100, 300, size)
sum = npy.random.randint(3000000, 20000000, size)
price_sqm = [round(sum[i] / hous[i]) for i in range(size)]
print(price_sqm)


hous_number = ['h_1','h_2','h_3','h_4','h_5','h_6','h_7','h_8','h_9','h_10','h_11','h_12','h_13','h14','h15']
plt.axhline(y = 50000, color = 'r')
plt.bar(hous_number, price_sqm)
plt.show()