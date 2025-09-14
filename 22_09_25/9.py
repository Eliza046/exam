c = 0

for i in open('09.txt'):
    a = [int(x) for x in i.split()]
    p = [x for x in a if a.count(x) > 1]
    n = [x for x in a if a.count(x) == 1]
    if len(p) > 0 and len(n) > 0:
        if (sum(p)/len(p)) < (sum(n)/len(n)):
            c += 1

print(c)