def f(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return f(n+2, m) + f(n+3, m) + f(n*2, m)

print(f(3,10)*f(10,25) - f(3,10)*f(10,17)*f(17,25))