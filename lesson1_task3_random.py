# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

scope = input("Введите границы диапазона для целого числа через пробел: ")
a, b = map(int, scope.split(' '))

if b > a:
    c = random.randint(a, b)
else:
    c = random.randint(b, a)
print(c)

scope = input("Введите границы диапазона для вещественного числа через пробел: ")
a, b = map(float, scope.split(' '))

if b > a:
    c = random.uniform(a, b)
else:
    c = random.uniform(b, a)
print(c)

scope = input("Введите границы диапазона для символа через пробел: ")
a, b = map(str, scope.split(' '))

if ord(b) > ord(a):
    c = random.randint(ord(a), ord(b))
else:
    c = random.randint(ord(b), ord(a))
print(chr(c))



