def f(n,m):
    if n==m:
        return 1
    elif n < m:
        return 0
    else:
        return f(n-2, m) + f(n//2,m)

print(f(80,40) * f(40, 1) - f(80,40) * f(40, 20)*f(20,1))