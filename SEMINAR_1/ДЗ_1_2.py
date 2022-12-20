a=input('Введите координаты первой точки "x,y"  ')
b=input('Введите координаты второй точки "x,y" ')
a_list=a.split(",")
b_list=b.split(",")
print(a_list)
print(b_list)
a_list_float=[float(i) for i in a_list]
b_list_float=[float(i) for i in b_list]
print(a_list_float)
print(b_list_float)
distance=((a_list_float[0]-b_list_float[0])**2+(a_list_float[1]-b_list_float[1])**2)**0.5
print(f'Расстояние между точками равно  {distance}')
