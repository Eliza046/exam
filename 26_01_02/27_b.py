from math import *

def centra(clu):
    a=[]
    for p1 in clu:
        summ = 0
        for p2 in clu:
            summ += dist(p1,p2)
        a.append([summ, p1])
    return min(a)[1]

data = []

with open('27var1b_2025-01-10T09_29_53.662193.txt') as f:
    for s in f:
        m = list(map(float, s.replace(',', '.').replace('"', '').split()))
        data.append(m)

print(data)

cluster = []

while data:
    cl = [data.pop()]
    for p1 in cl:
        sosedi = [p2 for p2 in data if dist(p1, p2) < 2.35]
        for p2 in sosedi:
            if p2 in data:
                data.remove(p2)
            cl.append(p2)
    cluster.append(cl)

print([len(cl) for cl in cluster])

px = 0
py = 0

for cl in cluster:
    px += centra(cl)[0]
    py += centra(cl)[1]

print(px/3 * 10000 //1, py/3 * 10000 //1)