F = {}
F[1] = 1
F[2] = 2

for n in range(3,101):
    F[n] = (F[n-1] - F[n-2]) * n

print(F[8])