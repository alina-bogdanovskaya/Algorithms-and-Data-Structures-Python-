# 4. Определить, какое число в массиве встречается чаще всего.

import random


def most_frequent(list):
    dict = {}
    most_frequent_count = 0
    most_frequent_item = ''

    for el in list:
        dict[el] = dict.setdefault(el, 0) + 1
        if dict[el] > most_frequent_count:
            most_frequent_count = dict[el]
            most_frequent_item = el

    return most_frequent_item


my_list = [random.randint(-10, 10) for _ in range(30)]
print(my_list)

print(f'Чаще всего в массиве встречается {most_frequent(my_list)}')
