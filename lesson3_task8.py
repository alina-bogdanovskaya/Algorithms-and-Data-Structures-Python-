# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

columns, rows = 5, 4

matrix = [[0]*columns for _ in range(rows)]

for row in matrix:
  row_sum = 0

  for i in range(columns - 1):
    row[i] = int(input("Введите число: "))
    row_sum += row[i]
  row[-1] = row_sum

for line in matrix:
  for item in line:
    print(f'{item: >4}', end = '')
  print()
