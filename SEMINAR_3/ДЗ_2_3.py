# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
stream=open('harvest.txt', mode='r', encoding='utf-8')
print(stream)
harvest=stream.readlines()[0].split()
print(type(harvest))
print(harvest)
stream.close()
letter ='а'
for flower in harvest:
    if flower[0] == letter:
        print(flower)

