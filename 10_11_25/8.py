from itertools import product
a = '0123'
c=0

for i in product(a, repeat=3):
    if (i[0] != '0') and (int(i[0]) + int(i[2]) > int(i[1])):
        c+=1

print(c)