# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_sum = 0
max = 0

while True:
  num = (input("Введите число или 0 для выхода: "))
  sum = 0
  if num == '0':
    break

  for el in num:
    sum += int(el)
    if sum > max_sum:
      max_sum = sum
      max = num

print(f'Наибольшее по сумме цифр число: {max}; сумма элементов: {max_sum}')
