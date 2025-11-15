from sys import setrecursionlimit

setrecursionlimit(10**6)

def F(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return 2*n*F(n-1) + F(n-3)
    elif n%2 == 1 and n > 1:
        return 3*n*F(n-2)

print(F(2026)/F(2021))