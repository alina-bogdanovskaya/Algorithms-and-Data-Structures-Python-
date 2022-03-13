# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

dict = {}

for el in range(2, 100):
  for item in range(2, 10):
    if el % item == 0:
      dict[item] = dict.setdefault(item, 0) + 1

print(dict)
