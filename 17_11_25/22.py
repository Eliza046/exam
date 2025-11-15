s = open("24.txt").read()
s = s.replace('CD', 'C D').split()
maxi = 0
for i in range(len(s)):
    r = ''.join(s[i:i + 141])
    maxi = max(maxi, len(r))
print(maxi)
