# Задача 2. В первой строке файла находится информация об 
# ассортименте мороженного, во второй - информация о том, 
# какое мороженное есть на складе. Выведите названия того 
# товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»

# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»

stream = open('icecream.txt', mode = 'r', encoding = 'utf-8')
raw_lines=stream.read()
stream.close()
lines_list = raw_lines.split('\n')
line_assortment = lines_list[0]
print(line_assortment)
line_store = lines_list[1]
print(line_store)
list_assortment = line_assortment.split(', ')
list_store = line_store.split(', ')
set_assortment = set(list_assortment)
set_store = set(list_store)
set_absence = set_assortment - set_store
print('ЗАКОНЧИЛИСЬ:')
for j in set_absence:
    print(j)
    

