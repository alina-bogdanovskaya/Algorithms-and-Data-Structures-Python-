# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

import math

print("Введите координаты точек А и В")
a = input("Введите координаты точки А через пробел (x1, y1): ")
b = input("Введите координаты точки B через пробел (x2, y2): ")

x_1, y_1 = map(float, a.split(' '))
x_2, y_2 = map(float, b.split(' '))

if x_1 == x_2 and y_1 == y_2:
    print("Точки совпадают")
elif math.isclose(x_1, x_2) == True:
    print(f'x = {x_1}')
else:
    k = (y_1 - y_2)/(x_1 - x_2)
    b = y_2 - k * x_2
    if k == 0:
        print(f'y = {b :.2f}')
    elif b == 0:
        print(f'y = {k :.2f}x')
    else:
        print(f'y = {k :.2f}x + {b :.2f}')
