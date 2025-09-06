def t(n):
    m = ''
    while n > 0:
        m = str(n%9) + m
        n = n // 9
    return m

m = t(81**17 + 3**24 - 45)
print(m.count('8'))