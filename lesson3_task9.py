# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

columns,rows = 5, 6

my_matrix = [[random.randint(-10, 10) for _ in range(columns)] for _ in range(rows)]

for line in my_matrix:
  for item in line:
    print(f'{item: >4}', end = '')
  print()

max_of_min_val = None

for col in range(0, columns):
    min_val = None
    for row in range(0, rows):
        if min_val is None or my_matrix[row][col] < min_val:
            min_val = my_matrix[row][col]

    if max_of_min_val is None or min_val > max_of_min_val:
        max_of_min_val = min_val

print(max_of_min_val)
