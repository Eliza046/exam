c = 0
b = 0

for i in range(84052, 84130+1):
    a = 0
    for j in range(1,i+1):
        if i % j == 0:
            a+=1
    if a > c:
        c = a
        b = i

print(c, b)
