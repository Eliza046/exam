def t(x):
    c = 0
    x = bin(x)[2:]
    for i in x:
        c += int(i)
    if c % 2 == 0:
        x = x + '00'
    else:
        x = x + '11'
    return int(x, 2)

print(t(28))