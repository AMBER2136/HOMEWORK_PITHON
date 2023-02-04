# Задача 1. В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random
def list_of_teams():
    for i in range(table_size):
        print(f'Результаты группы {i+1}: {table[i]}')

def arithmetic_mean(team):
    sum = 0
    for i in range(len(team)):
        sum = sum + team[i]
    mean_score = round(sum / len(team), 4)
    return mean_score

def list_of_scores():
    list_score = []
    for i in range(table_size):
        list_score.append(arithmetic_mean(table[i]))
    return list_score

def best_score():
    best_score = 0
    for i in range(table_size):
        if list_score[i] > best_score:
            best_score = list_score[i]
            team = i + 1
    print(f'Лучший средний балл - {best_score} у группы № {team}')

table_size = 4
table = []
for _ in range(table_size):
    team = [random.randint(2, 5) for i in range(0, random.randint(20, 31))]
    table.append(team)

for l in table:
    print(l)

list_of_teams()

for i in range(table_size):
    print(f'Средний балл группы {i+1} = {(arithmetic_mean(table[i]))}')

list_score = (list_of_scores())
best_score()



