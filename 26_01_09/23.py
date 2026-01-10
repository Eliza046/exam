def f(n,m):
    if n==m:
        return 1
    elif n>m:
        return 0
    else:
        return f(n+1,m) + f(n*2,m) + f(n*3,m)

print(f(1,11)*f(11,25) - f(1,11)*f(11,15)*f(15,25))