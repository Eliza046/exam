m = 0

for i in range(450000000,456789012):
    x = bin(i)[2:]
    if i%2==0:
        x = '11' + x
    else:
        x = '1'+x+'10'
    x = int(x,2)
    m = max(m,x)

print(m)