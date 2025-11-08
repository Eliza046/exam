f = open("27-A.txt")
n = int(f.readline())
a = [int(s) for s in f]
k = 0
for i in range(len(a)):
    s = 0
    for j in range(i,len(a)):
        s += a[j]
        if s % 999 == 0:
            k+=1
print(k)

f = open("27-B.txt")
n = int(f.readline())
a = [int(s) for s in f]
k = 0
for i in range(len(a)):
    s = 0
    for j in range(i,len(a)):
        s += a[j]
        if s % 999 == 0:
            k+=1
print(k)