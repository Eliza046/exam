f = open('demo_2025_24.txt').read()

m=0

for i in range(len(f)-1):
    for j in range(i+m, len(f)):
        if (f[i+m:j+1].count('-') == 1 and f[i+m:j+1].count('*') == 0) or (f[i+m:j+1].count('*') == 1 and f[i+m:j+1].count('-') == 0):
            m = max(m, j-i-m+1)

print(m)

