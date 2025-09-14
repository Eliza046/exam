for i in range(210235, 210300+1):
    a = []
    for x in range(2, i//2+1):
        if i % x == 0:
            a.append(x)
    if len(a) == 4:
        print(i)
        print(a)