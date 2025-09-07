d = open('24.txt')
t = d.read()
mac=0
a=0
i=0
while i<len(t)-2:
    if t[i] in 'CDF' and t[i+1] in 'CDF' and t[i+2] in 'AO':
        a += 1
        i+=3
        mac=max(mac, a)
    else:
        a = 0
        i+=1
print(mac)