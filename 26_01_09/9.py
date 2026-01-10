a = []
c=0

with open('1_9.txt') as f:
    for s in f:
        a.append(s.strip())

for i in a:
    m = [int(x) for x in i.split()]
    n = [x for x in m if m.count(x) == 1]
    if len(n) == 5:
        if (max(m) + min(m)) * 2 <= (sum(m) - (max(m) + min(m))):
            c+=1

print(c)