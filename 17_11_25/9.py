c = 0

with open('9(1).txt') as f:
    for s in f:
        s = s.strip()
        a = [int(x) for x in s.split()]
        n = [x for x in a if a.count(x)==1]
        p = [x for x in a if a.count(x) != 1]
        p = set(p)
        l = [a.count(x) for x in p]
        if l.count(3)==1 and len(p)==1 and sum(p)**2 > sum(n)**2:
            c+=1

print(c)