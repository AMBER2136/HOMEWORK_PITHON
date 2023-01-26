# Задача 3. Найдите все простые несократимые дроби, 
# лежащие между 0 и 1, знаменатель которых не превышает 11.
list_numerator = list(range(1,11))
print(f'Числители: {list_numerator}')
list_denominator = list(range(1,12))
print(f'Знаменатели: {list_denominator}')
print('Простые несократимые дроби: ')
for j in list_numerator:
    for i in list_denominator:
        if (list_numerator[j-1] / list_denominator[i-1] < 1) and not (list_numerator[j-1]%2==0 and list_denominator[i-1]%2==0) and not (list_numerator[j-1]%3==0 and list_denominator[i-1]%3==0):
            print(f'{list_numerator[j-1]}/{list_denominator[i-1]}',end=', ')
            



    