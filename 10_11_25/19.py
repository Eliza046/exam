def f(x, p):
    if x >= 40 or p > 2:
        return p == 2
    g = [f(x+1, p+1), f(x+4, p+1), f(x*2, p+1)]
    return any(g) if p%2 else all(g)

print([s for s in range(1, 39) if f(s, 0)])

def f(x, p):
    if x >= 40 or p > 3:
        return p == 3
    g = [f(x+1, p+1), f(x+4, p+1), f(x*2, p+1)]
    return any(g) if p%2==0 else all(g)

print([s for s in range(1, 39) if f(s, 0)])

def f(x, p):
    if x >= 40 or p > 4:
        return p == 2 or p==4
    g = [f(x+1, p+1), f(x+4, p+1), f(x*2, p+1)]
    return any(g) if p%2 else all(g)

print([s for s in range(1, 39) if f(s, 0)])