# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

x = 5
y = 6
print(bin(x))
print(bin(y))

# bitwise AND
a = x & y
print(a)
print(bin(a))

# bitwise OR
b = x | y
print(b)
print(bin(b))

# bitwise XOR
c = x ^ y
print(c)
print(bin(c))

# bitwise NOT
print(~x)
print(bin(~x))
print(~y)
print(bin(~y))

# bitwise shift right
d = x >> 2
print(d)
print(bin(d))

# bitwise shift left
e = x << 2
print(e)
print(bin(e))
