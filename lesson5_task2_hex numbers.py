from collections import defaultdict

# hex_dict_symbol = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# hex_dict_value = dict(zip(hex_dict_symbol.values(), hex_dict_symbol.keys()))

x = (input('Please enter first hexadecimal number: '))
y = (input('Please enter second hexadecimal number: '))


def hex_sum(x, y):
    hex_dict_symbol = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_dict_value = dict(zip(hex_dict_symbol.values(), hex_dict_symbol.keys()))

    x = list(x)
    y = list(y)

    x = x[::-1]
    y = y[::-1]
    z = defaultdict(int)

    if len(x) < len(y):
        x, y = y, x

    n, m = len(x), len(y)

    for i in range(n):
        if x[i] in hex_dict_symbol.keys():
            x[i] = hex_dict_symbol[x[i]]
        else:
            x[i] = int(x[i])
        a = x[i]
        if i < m:
            if y[i] in hex_dict_symbol.keys():
                y[i] = hex_dict_symbol[y[i]]
            else:
                y[i] = int(y[i])
            b = y[i]
        else:
            b = 0

        k = a + b
        u = k % 16
        v = k // 16

        z[i] += u
        v += z[i] // 16
        z[i] %= 16
        if v > 0:
            z[i + 1] += v

    for key, val in z.items():
        if val in hex_dict_value.keys():
            z[key] = hex_dict_value[val]
        else:
            z[key] = str(val)

    res = list(z.values())
    res.reverse()
    return res


def hex_mult(x, y):
    hex_dict_symbol = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_dict_value = dict(zip(hex_dict_symbol.values(), hex_dict_symbol.keys()))

    x = list(x)
    y = list(y)
    z = defaultdict(int)

    for i, item1 in enumerate(reversed(list(y))):
        if item1 in hex_dict_symbol.keys():
            item1 = hex_dict_symbol[item1]
        else:
            item1 = int(item1)
        for j, item2 in enumerate(reversed(list(x))):
            if item2 in hex_dict_symbol.keys():
                item2 = hex_dict_symbol[item2]
            else:
                item2 = int(item2)

            k = item1 * item2
            u = k % 16
            v = k // 16

            z[i + j] += u
            v += z[i + j] // 16
            z[i + j] %= 16
            if v > 0:
                z[i + j + 1] += v

    for key, val in z.items():
        if val in hex_dict_value.keys():
            z[key] = hex_dict_value[val]
        else:
            z[key] = str(val)

    res = list(z.values())
    res.reverse()
    return res


print(hex_sum(x, y))
print(hex_mult(x, y))
