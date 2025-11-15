F = {}
for n in range(1, 10 ** 6):
    if n <= 5:
        F[n] = 1000
    else:
        F[n] = n + 3 + F[n - 2]

print(3 * F[53079] - (F[53077] + F[53075] + F[53073]))