from itertools import *

def f(x,y,z,w):
    return ((x <= y) and (z or w)) <= ((x == w) or (y and (not(z))))

for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
    tab = [(0,0,a1,0), (1,a2,1,1), (0,a3,a4,a5)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in tab] == [0,0,0]:
                print(p)