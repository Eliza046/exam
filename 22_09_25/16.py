from sys import setrecursionlimit
setrecursionlimit(10**6)

def F(n):
    if n <= 2:
        return n
    else:
        return F(n-1) * F(n-2)

print(F(6))
