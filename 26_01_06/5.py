for i in range(1000):
    s = bin(i)[2:]
    if i%2==0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    s = int(s, 2)
    if s > 441:
        print(i)
        break