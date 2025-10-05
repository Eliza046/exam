a = [0, 1]

for x in a:
    for y in a:
        for z in a:
            for w in a:
                if (x<=(y == w))and(y == (w<=z)):
                    print(x, y, z, w)