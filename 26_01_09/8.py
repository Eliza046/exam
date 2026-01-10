from itertools import product

s = 'АПРСУ'
c = 0

for i in product(s, repeat=4):
    c += 1
    if i.count('А') == 0:
        print(i, c)
        break
