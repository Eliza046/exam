import itertools
x = "ПАРАБОЛА"
c = "ОА"
g = "ПРБЛ"
ar = itertools.permutations(x, 8) #Размещение
arl = []
for e in ar:
    arl.append(list(e))
a = set()
for e in arl:
    flag = True
    s = ""
    for i in range(len(e)-1):
        s += e[i]
        if (e[i] in c and e[i+1] in c) or (e[i] in g and e[i+1] in g):
            flag = False
    if flag:
        a.add(s)
print(len(a))