a = []
c=0

with open('09.txt') as f:
    for s in f:
        s = s.strip()
        a.append(s)


for i in a:
    d = [int(x) for x in i.split()]
    p = [x for x in d if d.count(x) > 1]
    n = [x for x in d if d.count(x) == 1]
    if len(p) > 0 and len(n) > 0 and (sum(p)/len(p))<(sum(n)/len(n)):
        c+=1

print(c)