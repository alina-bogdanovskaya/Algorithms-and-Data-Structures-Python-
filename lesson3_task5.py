# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

my_list = [random.randint(-10, 10) for _ in range(30)]
print(my_list)

max_negative_value = None
max_negative_value_pos = ''

for position, el in enumerate(my_list):
  if el >= 0:
    continue
  elif el < 0 and (max_negative_value is None or el > max_negative_value):
    max_negative_value = el
    max_negative_value_pos = position

print(f'Максимательный отрицательный элемент {max_negative_value} находится в массиве на позиции {max_negative_value_pos}')
