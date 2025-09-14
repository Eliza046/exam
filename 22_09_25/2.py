a = [0, 1]

for x in a:
    for y in a:
        for z in a:
            for w in a:
                if not(((x or not(y)) and (not(z)== w))<=(y and z)):
                    print(x, y, z, w)