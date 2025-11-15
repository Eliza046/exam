def f(x,y,p):
    if (x >= 48 or y>= 48) and p > 3:
        return p==1 and p == 3
    if x>y:
        game=[f(x+1,y,p+1), f(x+2,y,p+1), f(x+3,y,p+1), f(x, y*2, p+1)]
    if x<y:
        game=[f(x*2,y,p+1), f(x,y+1,p+1), f(x, y+2, p+1), f(x, y+3, p+1)]
    if x==y:
        game=[f(x+1,y,p+1), f(x+2,y,p+1), f(x+3,y,p+1), f(x, y+1, p+1), f(x, y+2, p+1), f(x, y+3, p+1)]
    return any(game) if p%2==0 else all(game)

print([s for s in range(1,30) if f(13,s,0)])