# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# n = int(input('Enter number of elements: '))
# sum = 0
# el = 1
#
# for i in range(n):
#   sum += el
#   el = el/-2
#
# print(sum)

def sequence_sum(el, n, coef):
  sum = 0

  for i in range(n):
    sum += el
    el = el * coef

  return sum

n = int(input('Enter number of elements: '))
el = 1
coef = -1/2

print(sequence_sum(el, n, coef))
