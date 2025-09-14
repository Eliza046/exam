s = open('241.txt').read().strip()
s = s.replace('XZZY', '*')
m = 1
c = 1
for i in range(1, len(s)):
    if s[i] != '*':
        c += 1
        m = max(m, c+3)
    else:
        c = 3
print(m)