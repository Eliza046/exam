t = open('17.txt')
d = t.readline()
a = []
c = 0

for i in d:
    if i[-2:] == '17':
        a.insert(0,i)

for i in range(1, len(d)):
    if ((len(d[i])==4 and len(d[i+1])==4
         and len(d[i-1])!=4) or (len(d[i])==4 and len(d[i-1])==4
                                 and len(d[i+1])!=4) or (len(d[i-1])==4 and len(d[i+1])==4
                                                         and len(d[i])!=4)) and (d[i -1]%5==0 or d[i]%5==0 or d[i+1]%5==0) and (d[i]+d[i+1]+d[i-1] > max(a)):
        c += 1

print(c)