a = ['0','1','2','3','4','5','6','7']
c = []

for x in a:
    for y in a:
        t=int(y+'04'+x+'5',11) + int('253'+x+y,8)
        if t%117 == 0:
            c.append(t)
print(min(c)//117)