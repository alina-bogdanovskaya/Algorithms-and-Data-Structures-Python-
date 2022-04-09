# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = random.randint(0, 30)
my_array = [random.randint(-20, 20) for _ in range(2*m + 1)]


def get_median(array):
    half_array = len(array) // 2

    for i in range(len(array)):
        u, v, k = 0, 0, 0
        for j in range(len(array)):
            if j == i:
                continue

            if array[j] < array[i]:
                u += 1
            elif array[j] > array[i]:
                v += 1
            else:
                k += 1

        if u == v == half_array:
            return array[i]
        elif u <= half_array and v <= half_array:
            u += (k - half_array - v)
            v += (k - half_array - u)
            return array[i]

    return None


print(f'Медианой массива {my_array} является {get_median(my_array)}')
