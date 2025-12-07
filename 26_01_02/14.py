from itertools import product

a = '01234567'

m = []

for x, y in product(a, repeat=2):
    t = int(x+'01'+y+'4', 9) + int(x+y+'544',8)
    if t % 89 ==0:
        m.append(t)

print(min(m)//89)

