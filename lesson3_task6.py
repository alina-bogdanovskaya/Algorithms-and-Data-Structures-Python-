# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

my_new_list = [random.randint(0, 100) for _ in range(50)]
print(my_new_list)

min_val, max_val = None, None
min_val_pos, max_val_pos = '', ''

for pos, el in enumerate(my_new_list):
  if max_val is None or el > max_val:
    max_val, max_val_pos = el, pos

  if min_val is None or el < min_val:
    min_val, min_val_pos = el, pos

start_point, end_point = 0, 0
sum = 0

if min_val_pos < max_val_pos:
  start_point, end_point = min_val_pos + 1, max_val_pos
else:
  start_point, end_point = max_val_pos + 1, min_val_pos

for i in range(start_point, end_point):
  sum += my_new_list[i]

print(f'Сумма элементов между {min_val} и {max_val} составляет {sum}')
