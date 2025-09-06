def t(n,m,k):
    return max(n,m,k) < n + m + k - max(n,m,k)

c=0
for A in range(1000):
        if all (not (t(x,11,16) == ((not(max(x,5) > 10))) and  t(4,A,x)) for x in range(1000)):
            print(A)
