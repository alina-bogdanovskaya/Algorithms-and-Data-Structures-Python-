# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Enter any number: ')
i = 0
j = 0

for el in num:
  if int(el) % 2 == 0:
    i += 1
  else:
    j += 1

print(f'Even count: {i} \nOdd count: {j}')
