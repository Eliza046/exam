from itertools import product, repeat

c = 0

for i in product('АВЛОР', repeat = 4):
    c += 1
    if i[0] == "Л":
        print(c)
        break