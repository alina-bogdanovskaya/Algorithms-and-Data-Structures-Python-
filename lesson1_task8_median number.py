# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

res = 0

if a > b:
    if a > c:
        if c > b:
            res = c
        else:
            res = b
    else:
        res = a
elif b > c:
    if a > c:
        res = a
    else:
        res = c
else:
    res = b

print(res)
