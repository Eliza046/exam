from itertools import product
c = 0

for i in product('01a',repeat=8):
    s = ''.join(i)
    if s.count('0') == 2 and s[0] != '0' and s.count('a') < 5:
        c+=9**s.count('1') * 6**s.count('a')
print(c)
