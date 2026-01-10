from math import *

def centra(clu):
    a = []
    r=[]
    for p1 in clu:
        summ = []
        for p2 in clu:
            summ.append(dist(p1,p2))
        a.append([max(summ), p1])
    cent = min(a)[1]
    for p in clu:
        r.append(dist(p,cent))
    return max(r)

data = []

with open('27A.txt') as f:
    for s in f:
        m = list(map(float, s.replace(',','.').replace('"', '').split()))
        data.append(m)

print(data)
cluster = []

while data:
    cl = [data.pop()]
    for p1 in cl:
        sosedi = [p2 for p2 in data if dist(p1, p2) < 1.5]
        for p2 in sosedi:
            if p2 in data:
                data.remove(p2)
            cl.append(p2)
    cluster.append(cl)

print([len(cl) for cl in cluster])
cluster.remove(cluster[0])
px = 0
print([len(cl) for cl in cluster])
for cl in cluster:
    px += centra(cl)
    print(centra(cl))

print(px/2*10000//1)