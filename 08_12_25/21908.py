from re import *

s = open('24_21908.txt').readline()

reg = f'[1-9ABCD][0-9ABCD]*[02468AC]'

m = max([x.group() for x in finditer(reg, s)], key=len)

print(len(m), m)