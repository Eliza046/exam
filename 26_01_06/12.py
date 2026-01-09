for i in range(100):
    n = '3' + '5'*i
    while '25' in n or '355' in n or '555' in n:
        n = n.replace('25','3', 1)
        n = n.replace('355','52', 1)
        n = n.replace('555','23', 1)
    if 2*n.count('2') + 3*n.count('3') + 5*n.count('5') == 27:
        print(i, n)
        break



