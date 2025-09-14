from fnmatch import fnmatch
for x in range(0, 10**10, 3147):
    if fnmatch(str(x), '1*4302?1'):
        print(x)