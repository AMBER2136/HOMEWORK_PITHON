# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.
import random
may_list = [random.randint(5, 18) for i in range(31)]
june_list = [random.randint(12, 23) for i in range(30)]
july_list = [random.randint(15, 24) for i in range(31)]
august_list = [random.randint(13, 25) for i in range(31)]
september_list = [random.randint(6, 19) for i in range(30)]

# print(may_list)
# print(june_list)
# print(july_list)
# print(august_list)
# print(september_list)

# may+++++++++++++++++++++++++++++++++++++++++++++++

interval = 7
may_mean_list =[]
dat_list = []
for i in range(0, (len(may_list)-interval+1)):
    sum_temp = 0
    for j in range((0 + i), (interval + i)):
        sum_temp += may_list[j]
        mean_temp = round(sum_temp / interval, 4)
        date_tuple = ((1 + i), (interval + i))
    may_mean_list.append(mean_temp)
    dat_list.append(date_tuple)
# print(may_mean_list)
# print(dat_list)

hot_may = 0
for i in range(len(may_mean_list)):
    if may_mean_list[i] > hot_may:
            hot_may = may_mean_list[i]
            index_h = i
print(f'Самый жаркий период мая - {hot_may} за интервал {dat_list[index_h][0]} - {dat_list[index_h][1]}')

cool_may = 100
for j in range(len(may_mean_list)):
    if may_mean_list[j] < cool_may:
            cool_may = may_mean_list[j]
            index_c = j
print(f'Самый холодный период мая - {cool_may} за интервал {dat_list[index_c][0]} - {dat_list[index_c][1]}')

# june+++++++++++++++++++++++++++++++++++++++++++++++++

interval = 7
june_mean_list =[]
dat_list = []
for i in range(0, (len(june_list)-interval+1)):
    sum_temp = 0
    for j in range((0 + i), (interval + i)):
        sum_temp += june_list[j]
        mean_temp = round(sum_temp / interval, 4)
        date_tuple = ((1 + i), (interval + i))
    june_mean_list.append(mean_temp)
    dat_list.append(date_tuple)
# print(june_mean_list)
# print(dat_list)

hot_june = 0
for i in range(len(june_mean_list)):
    if june_mean_list[i] > hot_june:
            hot_june = june_mean_list[i]
            index_h = i
print(f'Самый жаркий период июня - {hot_june} за интервал {dat_list[index_h][0]} - {dat_list[index_h][1]}')

cool_june = 100
for j in range(len(june_mean_list)):
    if june_mean_list[j] < cool_june:
            cool_june = june_mean_list[j]
            index_c = j
print(f'Самый холодный период июня - {cool_june} за интервал {dat_list[index_c][0]} - {dat_list[index_c][1]}')

# july+++++++++++++++++++++++++++++++++++++++++++++++++

interval = 7
july_mean_list =[]
dat_list = []
for i in range(0, (len(july_list)-interval+1)):
    sum_temp = 0
    for j in range((0 + i), (interval + i)):
        sum_temp += july_list[j]
        mean_temp = round(sum_temp / interval, 4)
        date_tuple = ((1 + i), (interval + i))
    july_mean_list.append(mean_temp)
    dat_list.append(date_tuple)
# print(july_mean_list)
# print(dat_list)

hot_july = 0
for i in range(len(july_mean_list)):
    if july_mean_list[i] > hot_july:
            hot_july = july_mean_list[i]
            index_h = i
print(f'Самый жаркий период июля - {hot_july} за интервал {dat_list[index_h][0]} - {dat_list[index_h][1]}')

cool_july = 100
for j in range(len(july_mean_list)):
    if july_mean_list[j] < cool_july:
            cool_july = july_mean_list[j]
            index_c = j
print(f'Самый холодный период июля - {cool_july} за интервал {dat_list[index_c][0]} - {dat_list[index_c][1]}')

# august+++++++++++++++++++++++++++++++++++++++++++++++

interval = 7
august_mean_list =[]
dat_list = []
for i in range(0, (len(august_list)-interval+1)):
    sum_temp = 0
    for j in range((0 + i), (interval + i)):
        sum_temp += august_list[j]
        mean_temp = round(sum_temp / interval, 4)
        date_tuple = ((1 + i), (interval + i))
    august_mean_list.append(mean_temp)
    dat_list.append(date_tuple)
# print(august_mean_list)
# print(dat_list)

hot_august = 0
for i in range(len(august_mean_list)):
    if august_mean_list[i] > hot_august:
            hot_august = august_mean_list[i]
            index_h = i
print(f'Самый жаркий период августа - {hot_august} за интервал {dat_list[index_h][0]} - {dat_list[index_h][1]}')

cool_august = 100
for j in range(len(august_mean_list)):
    if august_mean_list[j] < cool_august:
            cool_august = august_mean_list[j]
            index_c = j
print(f'Самый холодный период августа - {cool_august} за интервал {dat_list[index_c][0]} - {dat_list[index_c][1]}')

# september++++++++++++++++++++++++++++++++++++++++++++

interval = 7
september_mean_list =[]
dat_list = []
for i in range(0, (len(september_list)-interval+1)):
    sum_temp = 0
    for j in range((0 + i), (interval + i)):
        sum_temp += september_list[j]
        mean_temp = round(sum_temp / interval, 4)
        date_tuple = ((1 + i), (interval + i))
    september_mean_list.append(mean_temp)
    dat_list.append(date_tuple)
# print(september_mean_list)
# print(dat_list)

hot_september = 0
for i in range(len(may_mean_list)):
    if may_mean_list[i] > hot_september:
            hot_september = september_mean_list[i]
            index_h = i
print(f'Самый жаркий период сентября - {hot_september} за интервал {dat_list[index_h][0]} - {dat_list[index_h][1]}')

cool_september = 100
for j in range(len(september_mean_list)):
    if september_mean_list[j] < cool_september:
            cool_september = september_mean_list[j]
            index_c = j
print(f'Самый холодный период сентября - {cool_september} за интервал {dat_list[index_c][0]} - {dat_list[index_c][1]}')


