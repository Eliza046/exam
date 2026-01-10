for a in range(1,110):
    if all([((2*x + y) != 70) or (x < y) or (a<x) for x in range(1,101) for y in range(1,101)] ):
        print(a)