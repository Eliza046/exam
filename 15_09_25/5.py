def t(n):
    n = bin(n)[2:]
    summa = 0

    x = n.split()
    for  i in x:
        summa += int(i)
    n = str(n) + str(summa%2)

    n = int(n, 2)
    return n

for i in range(13, 50):
    m = t(i)
    if m < 100:
        print(m)