"""
Я выбрал три библиотеки: requests, pandas и matplotlib.

requests:

С помощью библиотеки requests можно отправлять HTTP-запросы и получать ответы от серверов. 
Благодаря ей можно просто удобно работать с протоколом HTTP.

"""


import requests

print(f"Пример работы библиотеки requests:\n")

# GET-запрос на сайт
response = requests.get('https://httpbin.org/ip')

# Вывод статуса-кода ответа
print(response.status_code)

# Вывод содержимого ответа
print(response.text)

# Отправляем POST-запрос с данными
data = {'key': 'value'}
response = requests.post('https://httpbin.org/ip', data=data)

# Вывод статуса-кода ответа
print(response.status_code)


"""
Возможности библиотеки requests:

Отправка HTTP-запросов (GET, POST, PUT, DELETE и т.д.)
Получение ответов от серверов
Работа с cookies и сессиями
Поддержка SSL/TLS

"""


"""
matplotlib

Благодаря библтотеки matplotlib можно создавать графики и визуализировать данные. 
Она имеет широкий спектр инструментов для создания различных типов графиков и диаграмм.

"""


import matplotlib.pyplot as plt

print(f"Пример работы библиотеки matplotlib:\n")

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Вывод графика
plt.plot(x, y)

# Заголовок и метки осей
plt.title('График')
plt.xlabel('X')
plt.ylabel('Y')

# Показываем график
plt.show()

"""
Возможности библиотеки matplotlib:

Создание различных типов графиков (линейные, столбчатые, круговые и т.д.)
Настройка внешнего вида графиков (цвета, шрифты, размеры и т.д.)
Добавление меток и заголовков к графикам
Сохранение графиков в различных форматах (PNG, PDF, EPS и т.д.)

"""

"""
numpy - это мощная библиотека для научных вычислений, 
которая обеспечивает эффективную работу с массивами и матрицами. 
Она позволяет выполнять сложные математические операции и анализировать 
данные с высокой производительностью.

"""
import numpy as np

print(f"Пример работы библиотеки numpy:\n")

# Массив из 10 случайных чисел
random_numbers = np.random.rand(10)
print(random_numbers)

# Сума всех элементов массива
sum_numbers = np.sum(random_numbers)
print(f"Сумма элементов массива: {sum_numbers}")

# Максимальное и минимальное значение в массиве
max_number = np.max(random_numbers)
min_number = np.min(random_numbers)
print(f"Максимальное число: {max_number}, Минимальное число: {min_number}")

# Выводим тип данных и размер массива
print(f"Тип данных: {random_numbers.dtype}, Размер: {random_numbers.size}")
