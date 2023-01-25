# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>
# [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
import random
size = 15
my_rand_list = list(random.randint(0,30) for _ in range(size))
print(my_rand_list)
j = random.randint(0,size-1)
print(j)
sequence = [my_rand_list[j]]
while j<size :
    j = random.randint(j, size)
    if j < size and my_rand_list[j] > sequence[-1]:
        sequence.append((my_rand_list[j]))
print(sequence)

    
