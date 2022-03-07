# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = (input('Please enter number to be reversed: '))
num_reversed = ''

for el in range(len(num) - 1, -1, -1):
    num_reversed = num_reversed + num[el]

print(num_reversed)
