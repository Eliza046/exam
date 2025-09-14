def t(x):
    a = ''
    while x > 0:
        a += str(x%3)
        x = x//3
    return a

a = 9 ** 8 + 3 ** 5 - 2
print(t(a).count('2'))