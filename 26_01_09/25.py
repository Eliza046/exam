count = 0
i = 500000001
while count < 5:
    halfI = i // 2
    dell = 1
    c = 0
    for j in range(2, halfI + 1):
        if i % j == 0:
            c += 1
            dell *= j
            if dell > i:
                break
            elif c == 5:
                print(dell)
                count += 1
                break
    i += 1