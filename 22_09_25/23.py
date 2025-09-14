s = open('24.txt').read().strip()
s = s.replace('A', '*')
s = s.replace('B', '*')
s = s.replace('C', '*')
m = 1
c = 1
for i in range(1, len(s)):
    if s[i-1]+s[i] != '**':
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)