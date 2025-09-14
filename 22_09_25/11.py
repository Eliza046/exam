def f(x):
    while not ('00' in x):
        x.replace('02', '101', 1)
        x.replace('11', '2', 1)
        x.replace('12', '21', 1)
        x.replace('010', '00', 1)
    return x

for i in range(69, 80):
    print(f('0'+'1'*i+'2'*i+'0'))