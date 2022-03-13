# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

another_list = [random.randint(0, 100) for _ in range(30)]
print(another_list)

min_val1, min_val2 = None, None

for el in another_list:
    if min_val1 is None or el <= min_val1:
        min_val2 = min_val1
        min_val1 = el
    elif min_val2 is None or el < min_val2:
        min_val2 = el

print(f'Наименьшие элементы: {min_val1}, {min_val2}')
