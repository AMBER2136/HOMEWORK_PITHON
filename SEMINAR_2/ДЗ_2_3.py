# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
str_1=str('treyk')
str_2=str('hyrtdeftnekryt')
print(str_1)
print(str_2)
len_1 = list(range(len(str_1)))
for i in (len_1):
    a = str_1 [i]
    print(f'{a}-{str_2.count(a)}',end =' / ')
    
