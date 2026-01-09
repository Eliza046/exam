f = open('17 (1).txt')
a = []
c=[]
s = []

for i in f.readlines():
    i = i.strip()
    s.append(int(i))
print(s)

for i in s:
    if str(i)[-1] == '7':
        a.append(i)

print(min(a), a)

for i in range(len(s)-1):
    if ((s[i] in a and s[i+1] not in a) or (s[i] not in a and s[i+1] in a)) and int(s[i]) ** 2 + int(s[i+1]) ** 2 < int(min(a))**2:
        c.append(int(s[i]) ** 2 + int(s[i+1]) ** 2)

print(len(c), max(c))