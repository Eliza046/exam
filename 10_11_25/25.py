count = 0
num = 700000
while count < 5:
	num += 1
	mx = 0
	mn = num + 1
	for i in range(2,int(num // 2)+1):
		if num % i == 0:
			mx = max(mx,i)
			mn = min(mn,i)
	M = mn + mx
	if (M != num + 1) and (M % 10 == 4):
		print(num, M)
		count += 1