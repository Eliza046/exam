a = [0, 1]

for x in a:
    for y in a:
        for z in a:
            for w in a:
                if (x or not(y))and not(y == z) and not(w):
                    print(x, y, z, w)