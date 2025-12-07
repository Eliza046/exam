F = {}
a = 1000000

for n in range(1,100000):
    if n < 4000:
        F[n] = n
    elif n %7==0:
        F[n] = n + F[n//7]
    else:
        F[n] = 567 + F[n-3]

    if F[n] > 80000:
        a = min(a,n)

print(a)
