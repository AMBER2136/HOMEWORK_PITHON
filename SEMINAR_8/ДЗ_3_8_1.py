# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите их даты.
import random
may_list = [random.randint(5, 18) for i in range(31)]
june_list = [random.randint(12, 23) for i in range(30)]
july_list = [random.randint(15, 24) for i in range(31)]
august_list = [random.randint(13, 25) for i in range(31)]
september_list = [random.randint(6, 19) for i in range(30)]
period_list = may_list + june_list + july_list + august_list + september_list
print(period_list)
print(len(period_list))

interval = 7
period_mean_list =[]
dat_list = []
for i in range(0, (len(period_list)-interval+1)):
    sum_temp = 0
    for j in range((0 + i), (interval + i)):
        sum_temp += period_list[j]
        mean_temp = round(sum_temp / interval, 4)
        date_tuple = ((1 + i), (interval + i))
    period_mean_list.append(mean_temp)
    dat_list.append(date_tuple)
print(period_mean_list)
print(dat_list)

hot_period = 0
for i in range(len(period_mean_list)):
    if period_mean_list[i] > hot_period:
            hot_period = period_mean_list[i]
            index_h = i
print(f'Самый жаркий период - {hot_period} за интервал {dat_list[index_h][0]} - {dat_list[index_h][1]}')

cool_period = 100
for j in range(len(period_mean_list)):
    if period_mean_list[j] < cool_period:
            cool_period = period_mean_list[j]
            index_c = j
print(f'Самый холодный период - {cool_period} за интервал {dat_list[index_c][0]} - {dat_list[index_c][1]}')

# Поиск месяца++++++++++++++++++++++++++++++++++++++++++++++++++++

if dat_list[index_h][0] < 32: month_h = 'мая'
if  31 < dat_list[index_h][0] < 62: month_h = 'июня'
if 61 < dat_list[index_h][0] < 93: month_h = 'июля'
if 92 < dat_list[index_h][0] < 124: month_h = 'августа'
if 123 < dat_list[index_h][0]: month_h ='сентября'
if dat_list[index_h][1] < 32: month_h_1 = 'мая'
if  31 < dat_list[index_h][1] < 62: month_h_1 = 'июня'
if 61 < dat_list[index_h][1] < 93: month_h_1 = 'июля'
if 92 < dat_list[index_h][1] < 124: month_h_1 = 'августа'
if 123 < dat_list[index_h][1]: month_h_1 ='сентября'

if dat_list[index_c][0] < 32: month_c = 'мая'
if  31 < dat_list[index_c][0] < 62: month_c = 'июня'
if 61 < dat_list[index_c][0] < 93: month_c = 'июля'
if 92 < dat_list[index_c][0] < 124: month_c = 'августа'
if 123 < dat_list[index_c][0]: month_c ='сентября'
if dat_list[index_c][1] < 32: month_c_1 = 'мая'
if  31 < dat_list[index_c][1] < 62: month_c_1 = 'июня'
if 61 < dat_list[index_c][1] < 93: month_c_1 = 'июля'
if 92 < dat_list[index_c][1] < 124: month_c_1 = 'августа'
if 123 < dat_list[index_c][1]: month_c_1 ='сентября'

# Поиск даты+++++++++++++++++++++++++++++++++++++++++++++++

if dat_list[index_h][0] - 32 < 0: data_h = dat_list[index_h][0]
if dat_list[index_h][0] - 31 > 0: data_h = dat_list[index_h][0] - 31
if dat_list[index_h][0] - 61 > 0: data_h = dat_list[index_h][0] - 61
if dat_list[index_h][0] - 92 > 0: data_h = dat_list[index_h][0] - 92
if dat_list[index_h][0] - 123 > 0: data_h = dat_list[index_h][0] - 123

if dat_list[index_h][1] - 32 < 0: data_h_1 = dat_list[index_h][1]
if dat_list[index_h][1] - 31 > 0: data_h_1 = dat_list[index_h][1] - 31
if dat_list[index_h][1] - 61 > 0: data_h_1 = dat_list[index_h][1] - 61
if dat_list[index_h][1] - 92 > 0: data_h_1 = dat_list[index_h][1] - 92
if dat_list[index_h][1] - 123 > 0: data_h_1 = dat_list[index_h][1] - 123

if dat_list[index_c][0] - 32 < 0: data_c = dat_list[index_c][0]
if dat_list[index_c][0] - 31 > 0: data_c = dat_list[index_c][0] - 31
if dat_list[index_c][0] - 61 > 0: data_c = dat_list[index_c][0] - 61
if dat_list[index_c][0] - 92 > 0: data_c = dat_list[index_c][0] - 92
if dat_list[index_c][0] - 123 > 0: data_c = dat_list[index_c][0] - 123

if dat_list[index_c][1] - 32 < 0: data_c_1 = dat_list[index_c][1]
if dat_list[index_c][1] - 31 > 0: data_c_1 = dat_list[index_c][1] - 31
if dat_list[index_c][1] - 61 > 0: data_c_1 = dat_list[index_c][1] - 61
if dat_list[index_c][1] - 92 > 0: data_c_1 = dat_list[index_c][1] - 92
if dat_list[index_c][1] - 123 > 0: data_c_1 = dat_list[index_c][1] - 123

print(f'Самый жаркий период - {hot_period} за интервал {data_h} {month_h} - {data_h_1} {month_h_1}')
print(f'Самый холодный период - {cool_period} за интервал {data_c} {month_c} - {data_c_1} {month_c_1}')
