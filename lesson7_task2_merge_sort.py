# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

array_to_sort = [random.uniform(0, 50) for _ in range(25)]


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2

    left_part = merge_sort(array[:mid])
    right_part = merge_sort(array[mid:])

    def merge(left, right):

        if len(left) == 0:
            return right

        if len(right) == 0:
            return left

        res = []
        i_left = i_right = 0

        while len(res) < len(left) + len(right):
            if left[i_left] <= right[i_right]:
                res.append(left[i_left])
                i_left += 1
            else:
                res.append(right[i_right])
                i_right += 1

            if i_right == len(right):
                res += left[i_left:]
                break

            if i_left == len(left):
                res += right[i_right:]
                break

        return res

    return merge(left_part, right_part)


print(f'Исходный массив: \n{array_to_sort} \nОтсортированный массив: \n{merge_sort(array_to_sort)}')
