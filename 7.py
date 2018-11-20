def Sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime
z = []
x = Sieve(104730)
for i in range(2, 104730):
	if x[i]:
		z.append(i)
t = int(input())
for _ in range(t):
	n = int(input())
	print(z[n-1])