# Задача 1. Задайте список случайных чисел от 1 до 10, 
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random
size = 10
my_rand_list=[random.randint(0,10) for _ in range(10)]
print(my_rand_list)
res_list = list(filter(lambda x: x>5, my_rand_list))
print(res_list)

