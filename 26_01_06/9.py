a = []

with open('9_58322.txt') as f:
    for s in f:
        a.append(s.strip())

c=0

for i in a:
    m = [int(x) for x in i.split()]
    m = sorted(m)
    if (m[3]**2 > m[1]*m[0]*m[2]) or (((m[1] - m[0]) == (m[2] - m[1])) and ((m[3] - m[2]) == (m[2] - m[1]))):
        c+=1

print(c)