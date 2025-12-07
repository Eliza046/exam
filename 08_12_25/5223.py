s = open('24_5223.txt').readline()

m = 0

s = s.replace('DD', 'D D')
print(s)

m = list(map(str, s.split(' ')))
print(m)

a = 0

for i in m:
    if 'FE' in i:
        a = max(a, len(i))

print(a)