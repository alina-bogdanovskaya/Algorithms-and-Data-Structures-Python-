# Урок 2, задание 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

import sys
from collections import deque


def show_cumulative_size(x):

    cumulative_size = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                cumulative_size += show_cumulative_size(xx)
        elif not isinstance(x, str):
            for xx in x:
                cumulative_size += show_cumulative_size(xx)

    return cumulative_size


num = (input('Please enter number to be reversed: '))


def reverse_num1(num):
    num_reversed = ''

    for el in range(len(num) - 1, -1, -1):
        num_reversed = num_reversed + num[el]

    print(num_reversed)

    my_variables = [num, len(num), num_reversed]
    print(f'Total memory used: {show_cumulative_size(my_variables)} bytes')


def reverse_num2(num):
    num_list = list(num)
    reversed_list = list(reversed(num_list))
    num_reversed = ''.join(reversed_list)

    print(num_reversed)

    my_variables = [num, num_list, reversed_list, num_reversed]
    print(f'Total memory used: {show_cumulative_size(my_variables)} bytes')


def reverse_num3(num):
    num_list = list(num)
    reversed_list = deque()
    reversed_list.extendleft(num_list)
    num_reversed = ''.join(reversed_list)

    print(num_reversed)

    my_variables = [num, num_list, reversed_list, num_reversed]
    print(f'Total memory used: {show_cumulative_size(my_variables)} bytes')


reverse_num1(num)
reverse_num2(num)
reverse_num3(num)

# print(sys.version, sys.platform)

# 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] win32

# Please enter number to be reversed: 123456789
# 987654321
# Total memory used: 224 bytes
# 987654321
# Total memory used: 1416 bytes
# 987654321
# Total memory used: 1856 bytes

# Please enter number to be reversed: 123456789123456789123456789
# 987654321987654321987654321
# Total memory used: 260 bytes
# 987654321987654321987654321
# Total memory used: 3556 bytes
# 987654321987654321987654321
# Total memory used: 3836 bytes

# Please enter number to be reversed: 887767718899002736554566772889966665777464553541333134435566788998876554433216756
# 657612334455678899887665534431333145355464777566669988277665455637200998817767788
# Total memory used: 368 bytes
# 657612334455678899887665534431333145355464777566669988277665455637200998817767788
# Total memory used: 9984 bytes
# 657612334455678899887665534431333145355464777566669988277665455637200998817767788
# Total memory used: 10304 bytes

#  Первый вариант с использование простейшего цикла значительно выигрывает по памяти,
#  поскольку не создает лишних промежуточных переменных.
#  Также при увеличении размера входных данных потребляеамя память растет гораздо медленнее.
