f = open('17 (2).txt')
a = []
c=[]

for s in f:
    a.append(int(s))

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i] + a[j]) % 10 == 0:
            c.append(a[i] + a[j])

print(len(c), max(c))