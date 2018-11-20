t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	x = input()
	m = []
	for i in range(k, n):
		p = x[i-k:i]
		s = 1
		for i in p:
			s*=int(i)
		m.append(s)
	print(max(m))