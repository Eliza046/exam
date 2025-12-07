def f(n):
    s = ''
    while n != 0:
        s = str(n %3) + s
        n //= 3
    return s

a=[]

for n in range(1,10000):
    r = f(n)

    if n % 3==0:
        r += r[-2:]
    else:
        r += f((n%3)*5)

    t = int(r,3)

    if t <= 173:
        a.append(t)

print(max(a))
