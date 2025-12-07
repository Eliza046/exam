from itertools import product

a = '0123456'
c=0

for i in product(a, repeat=4):
    if i[0] > i[1] > i[2] > i[3]:
        c+=1

print(c)