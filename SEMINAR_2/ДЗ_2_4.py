# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
l = list(range(-5,6,1))
shift = 3
print(l)
l_len = len(l)
l_list = list(range(l_len - shift))
buf = l[l_len - shift:]
for i in l_list:
    l[l_len-1-i] = l[l_len-1-shift-i]
del l[0:shift]
result = buf + l
print(result) 




