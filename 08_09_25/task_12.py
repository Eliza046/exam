n = '1' * 99

while '111' in n:
    n = n.replace('111', '22', 1)
    n = n.replace('222', '11', 1)

print(n)