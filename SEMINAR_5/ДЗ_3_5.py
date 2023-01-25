# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

import random
size = 10
my_rand_list = list(random.randint(0,10) for _ in range(size))
print(my_rand_list)
bool_map = list(map(lambda w: my_rand_list.count(w) > 1, my_rand_list))
lst_filter = list(filter(lambda w: my_rand_list.count(w) == 1, my_rand_list))
print(lst_filter)
print(bool_map)
replay = bool_map.count(True)
print(f'В списке {len(lst_filter)} уникальных элементов.')
print(f'В списке {replay} повторяющихся элементов.')


