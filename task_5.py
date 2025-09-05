def t(n):
    m = ''
    while n > 0:
        m = str(n%3) + m
        n = n // 3
    return m

c = 0
for i in range(1, 100):
    m = t(i)
    if i%3==0:
        m = m + m[-2:]
    else:
        m = m+t((i%3)*5)
    if int(m, 3) > int(c) and int(m,3 ) < 173:
        c = int(m, 3)
print(c)
