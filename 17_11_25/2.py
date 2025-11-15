a = [0, 1]

for x in a:
    for y in a:
        for z in a:
            for w in a:
                if not((x<=(z<=w))and(z<=(y==(not(w))))):
                    print(x, y, z, w)