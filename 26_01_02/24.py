f = open('1_24.txt').read()

m = 0
for i in range(len(f)):
    for j in range(i, len(f)-1):
        if (f[j] in 'QWR' and f[j+1] in 'QWR') or (f[j] in '124' and f[j+1] in '124'):
            m = max(m, j-i+1)
            break

print(m)