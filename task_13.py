c = 0
for x in range(2**3):
    if (15 + bin(x).count('1')) % 4 != 0:
        c += 1
print(c)