# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

my_list = [random.randint(-100, 100) for _ in range(30)]
print(my_list)

min_val, max_val = None, None
min_val_pos, max_val_pos = '', ''

for pos, el in enumerate(my_list):
  if max_val is None or el > max_val:
    max_val, max_val_pos = el, pos

  if min_val is None or el < min_val:
    min_val, min_val_pos = el, pos

my_list[max_val_pos], my_list[min_val_pos] = my_list[min_val_pos], my_list[max_val_pos]
print(my_list)
