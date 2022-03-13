# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random

first_list = [random.randint(0, 100) for _ in range(30)]
print(first_list)

second_list = []

for pos, el in enumerate(first_list):
  if el % 2 == 0:
    second_list.append(pos)

print(second_list)
