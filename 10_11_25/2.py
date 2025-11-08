a = [0, 1]

for x in a:
    for y in a:
        for z in a:
            for w in a:
                if not(((x<=y)==(z<=w)) or (x and w)):
                    print(x, y, z, w)