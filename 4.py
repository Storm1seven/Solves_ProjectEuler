def checkpal(a):
	if a[::-1] == a:
		return True
	else:
		return False
t = int(input())
master = []
for i in range(100, 1000):
	for j in range(100, 1000):
		if checkpal(str(i*j)):
			master.append(i*j)
master = list(set(master))
master.sort()
for _ in range(t):
	n = int(input())
	for i in range(len(master)):
		if master[i] >= n:
			print(master[i-1])
			break