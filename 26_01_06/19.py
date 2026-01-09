def f(x, p):
    if x <= 19 or p > 2:
        return p==2
    g = [f(x-1, p+1)]
    if x % 3 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-2, p+1))
    if x % 5 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-3, p+1))
    return any(g) if p%2 else all(g)

print([s for s in range(19, 60) if f(s,0)])


#20

def f(x, p):
    if x <= 19 or p > 1:
        return p==1
    g = [f(x-1, p+1)]
    if x % 3 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-2, p+1))
    if x % 5 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-3, p+1))
    return any(g) if p%2==0 else all(g)

print([s for s in range(19, 60) if f(s,0)])


def f(x, p):
    if x <= 19 or p > 3:
        return p==3
    g = [f(x-1, p+1)]
    if x % 3 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-2, p+1))
    if x % 5 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-3, p+1))
    return any(g) if p%2==0 else all(g)

print([s for s in range(19, 80) if f(s,0)])

#21

def f(x, p):
    if x <= 19 or p > 2:
        return p==2
    g = [f(x-1, p+1)]
    if x % 3 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-2, p+1))
    if x % 5 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-3, p+1))
    return any(g) if p%2 else all(g)

print([s for s in range(19, 80) if f(s,0)])


def f(x, p):
    if x <= 19 or p > 4:
        return p==4 or p==2
    g = [f(x-1, p+1)]
    if x % 3 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-2, p+1))
    if x % 5 == 0:
        g.append(f(x//3, p+1))
    else:
        g.append(f(x-3, p+1))
    return any(g) if p%2 else all(g)

print([s for s in range(19, 80) if f(s,0)])