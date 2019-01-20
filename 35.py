def prepareset(i):
    numset = []
    st = i+i
    for p in range(len(i)):
        string = ''
        for q in range(len(i)):
            string+=st[p+q]
        numset.append(int(string))
    return numset
def Sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime
n = int(input())
prime = Sieve(n)
s = set([])
for i in range(n):
    if '0' not in str(i) and '2' not in str(i) and '4' not in str(i) and '5' not in str(i) and '6' not in str(i) and '8' not in str(i):
        if i not in s:
            numset = prepareset(str(i))
            if all(prime[j] for j in numset):
                for i in numset:
                    s.add(i)
print(sum(s)-1+2+5)