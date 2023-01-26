# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве 
# последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
from random import randint as rint
def compare(c,d):
    if c==d : 
        return True
    else :
        return False

size = 15
real = 231
list_real = [int(i) for i in str(real)]
print(list_real)
# my_list = list(rint(0,20) for _ in range(size)) 
my_list = [1,4,5,2,3,1,6,7,8,9,6,2,3,1] # Это проверочный, демонстрационный массив!
print(my_list)
i,j=0,3
count = 0
for _ in range(size):
      e = my_list[i:j]
      print(e)
      bool = compare(e, list_real)
      print(compare(e, list_real))
      i+=1
      j+=1
      if bool == True: 
       print('Обнаружено совпадение')
       count += 1
      if bool == False: print('Совпадения нет')
print(count)
if count > 0: print(f'Обнаружено {count} совпадений')
