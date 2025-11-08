m = 0

with open("17.txt") as f:
    d = 0
    for s in f:
        s = s.strip()
        a = [int(x) for x in s.split()]
        for i in a:
            if i % 100 == 19:
                m = max(m, i)

        for i in range(1, len(a)):
            b = [a[i - 1], a[i], a[i + 1]]
            c = [len(str(a[i-1])), len(str(a[i])), len(str(a[i+1]))]
            if (c.count(4) == 2) and (b[0]%3==0 or b[1]%3==0 or b[2]%3==0) and sum(b)>m:
                d+=1

print(d)

