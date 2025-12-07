from re import*

s = open('24_21421.txt').readline()

reg = f'[1-9AB][0-9AB]*[02468A]'

m = max([x.group() for x in finditer(reg,s)], key=len)

print(len(m), m)