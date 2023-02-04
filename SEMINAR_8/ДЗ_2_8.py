# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
import random

row_size = 6
column_size = 6
matrix = []
for _ in range(column_size):
    line = [random.randint(0, 9) for i in range(row_size)]
    matrix.append(line)
print(matrix)

for row in matrix:
    print(row)

i = 0  
j = 0
count = 0
diagonal_sum = 0
for _ in range(row_size):
    diagonal_sum += matrix[i + count][j + count]
    count +=1
print(diagonal_sum)
# i = 0
# j = 0
count_i = 0
line_sum_list = []
for _ in range(column_size):
    count_j = 0
    line_sum = 0
    for _ in range(row_size):
        line_sum += matrix[i + count_i][j + count_j]
        count_j +=1
    line_sum_list.append(line_sum)
    count_i += 1
print(line_sum_list)

print('Это строки: ', end = '')
count_more = 0
for i in range(column_size):
    if line_sum_list[i] > diagonal_sum:
        print(f'{(i+1)}, ',end =' ')
        count_more += 1
print(f'Количество строк = {count_more}')
if count_more == 0:
    print('Таких строк нет')

