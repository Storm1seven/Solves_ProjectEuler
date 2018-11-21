def Sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime
x = Sieve(1000000)
count = 0
z = ["x", 0, 2]
for i in range(3, 1000000):    
    if x[i]:
        z.append(z[i-1]+i)
    else:
        z.append(z[i-1])
t = int(input())
for _ in range(t):
    n = int(input())
    print(z[n])