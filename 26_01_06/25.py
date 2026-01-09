from fnmatch import fnmatch

s = '24680'

for i in range(0, 10**10, 2026):
    if fnmatch(str(i), '7?23?64*8') and  str(i)[1] in s and str(i)[4] in s:
        print(i)