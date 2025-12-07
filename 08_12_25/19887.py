s = open('24.23_19887.txt').readline()

k = 1
m = 0

for i in range(len(s)-1):
    if (int(s[i])%2) != (int(s[i+1])%2):
        k += 1
        m = max(m, k)
    else:
        k = 1

print(m)