for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(not(x <= z) or (y == w) or y):
                    print(x, y, z, w)