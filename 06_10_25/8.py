c = 0

for i in open('69914.txt'):
    a = [int(x) for x in i.split()]
    p = [x for x in a if a.count(x) > 1]
    n = [x for x in a if a.count(x) == 1]
    if len(p) == 3:
        if p[0] >= sum(n)/3:
            c += 1

print(c)