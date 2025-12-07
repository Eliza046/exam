def f(x, p):
    if x <= 25 or p > 2:
        return p==2
    g = [f(x-3,p+1), f(x-6, p+1), f(x//3, p+1)]
    return any(g) if p%2 else all(g)

print([s for s in range(25, 600) if f(s,0)])


def f(x, p):
    if x <= 25 or p > 3:
        return p==3
    g = [f(x-3,p+1), f(x-6, p+1), f(x//3, p+1)]
    return any(g) if p%2==0 else all(g)

print([s for s in range(25, 600) if f(s,0)])


def f(x, p):
    if x <= 25 or p > 4:
        return p==4 or p==2
    g = [f(x-3,p+1), f(x-6, p+1), f(x//3, p+1)]
    return any(g) if p%2 else all(g)

print([s for s in range(25, 600) if f(s,0)])