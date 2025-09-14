def f(x):
    while '111' in x:
        x.replace('111', '2', 1)
        x.replace('222', '11', 1)
    return x

print(f('1'*78))