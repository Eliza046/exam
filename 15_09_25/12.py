def t(n):
    while ('52' in n) or ('2222' in n) or ('1122' in n):
        if '52' in n:
            n.replace('52', '11', 1)
        if '2222' in n:
            n.replace('2222', '5', 1)
        if '1122' in n:
            n.replace('1122', '25', 1)
    return n

c = 0

for i in range(3, 1000):
    n = '5'+'2'*i
    m = t(n)
    if sum(list(map(int, m))) == 64:
        c = i
print(c)