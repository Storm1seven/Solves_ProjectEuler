def factors(n):
	a = set([])
	for i in range(1, int(n**0.5)+1):
		if n%i == 0:
			a.add(i)
			a.add(n//i)
	return sum(list(a)) - n
a = [0]*(10**5 + 1)
for i in range (len(a)):
	a[i]+=factors(i)
z = set([])
for i in range(len(a)):
	if a[i] <= 10**5:
		if a[a[i]] == i and a[i]!=i:
			z.add(a[i])
			z.add(i)
z = list(z)
z.sort()
for _ in range(int(input())):
	s = 0
	n = int(input())
	for i in z:
		if i <= n:
			s+=i
		else:
			break
	print(s)