f = open('inf_22_10_20_18.txt')
a = [float(s.strip()[1:-2].replace(',', '.')) for s in f]

m = 0
c = 0

for i in range(len(a)-1):
    if a[i] > a[i+1]:
        c += a[i]
    else:
        c += a[i]
        m = max(m, c)
        c = 0

print(m)