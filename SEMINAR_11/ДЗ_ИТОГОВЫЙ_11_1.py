# Задача 1. Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as plt

x_list = []
y_list = []

for x in range(-10, 11):
    y = 5*x**2 + 10*x - 30

    x_list.append(x)
    y_list.append(y)

    plt.axhline(y = 0)
    plt.plot(y_list)
    plt.show()

# Результат: 6,401 и 11,597