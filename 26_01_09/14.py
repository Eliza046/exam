s = 49**7 + 7**21 - 7
n = ''

while s != 0:
    n = str(s%7) + n
    s //= 7

print(n.count('6'))