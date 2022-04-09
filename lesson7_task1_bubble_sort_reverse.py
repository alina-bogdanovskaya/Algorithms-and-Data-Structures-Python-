# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

my_array = [random.randrange(-100, 100) for _ in range(25)]


def bubble_sort_reverse(array):
    for i in range(len(array)):
        already_sorted = True

        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    return array


print(f'Исходный массив: \n{my_array} \nОтсортированный массив: \n{bubble_sort_reverse(my_array)}')
