f = open('24.txt')

s = f.readline().replace('ad', 'a d').replace('da', 'd a')

w = list(map(len, s.split()))

print(max(w))