c = 0

for i in open('09 (1).txt'):
    a = [int(x) for x in i.split()]
    p = [x for x in a if a.count(x) > 1]

    if a.count(min(a)) == 1 and len(p) > 0 and max(a) / ((sum(a) - max(a))/5) > 3:
        c += 1
print(c)