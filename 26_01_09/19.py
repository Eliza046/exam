def f(x,y,p):
    if (x+y)<=165 or p>2:
        return p==2
    g = [f(x-2,y,p+1),f(x,y-2,p+1), f(x//3,y,p+1),f(x,y//3,p+1)]
    return any(g) if p%2 else any(g)

print(max([s for s in range(165, 10000) if f(17,s,0)]))

def f(x,y,p):
    if (x+y)<=165 or p>3:
        return p==3
    g = [f(x-2,y,p+1),f(x,y-2,p+1), f(x//3,y,p+1),f(x,y//3,p+1)]
    return any(g) if p%2==0 else all(g)

print([s for s in range(149, 1000) if f(17,s,0)])


def f(x,y,p):
    if (x+y)<=165 or p>2:
        return p==2
    g = [f(x-2,y,p+1),f(x,y-2,p+1), f(x//3,y,p+1),f(x,y//3,p+1)]
    return any(g) if p%2 else all(g)

print([s for s in range(165, 10000) if f(17,s,0)])

def f(x,y,p):
    if (x+y)<=165 or p>4:
        return p==2 or p==4
    g = [f(x-2,y,p+1),f(x,y-2,p+1), f(x//3,y,p+1),f(x,y//3,p+1)]
    return any(g) if p%2 else all(g)

print([s for s in range(165, 10000) if f(17,s,0)])


