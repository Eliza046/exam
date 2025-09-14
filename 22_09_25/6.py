def s(x):
    x = str(x)
    if int(x[0]) % 2 != 0 and int(x[1]) % 2 != 0 and int(x[2]) % 2 != 0 and int(x[3]) % 2 != 0:
        x_1 = (int(x[0]) + int(x[1]))
        x_2 = (int(x[2]) + int(x[3]))
        if x_1 > x_2:
            return str(x_2) + str(x_1)
        else:
            return str(x_1) + str(x_2)

c = 0

for i in range(1000, 10000):
    if s(i) == '616':
        c+=1
        print(i)

print(c)