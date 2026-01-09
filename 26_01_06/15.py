def f(x):
    A = (a1 <= x <= a2)
    P = (19 <= x <= 84)
    Q = (4 <= x <= 51)
    return Q <= (((not(P)) <= (not(Q and (not(A))))))

r = []

d = [y for x in (4,19,51,84) for y in (x, x+0.1,x-0.1)]
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) for x in d):
            r += [a2-a1]

print(round(min(r)))