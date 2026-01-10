from itertools import product
c=0
for i in product([0,1], repeat = 12):
    if i.count(1) == 2:
        print(i)
        c +=1
print(c)