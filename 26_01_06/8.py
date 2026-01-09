import itertools
otv = []
for i in range(2,14):
    combs = [''.join(j) for j in itertools.combinations('123456789ABC', i)]
    otv.append(len(combs))
print(sum(otv))