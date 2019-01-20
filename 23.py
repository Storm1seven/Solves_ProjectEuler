def sum_fac(n):
    s = set([])
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            s.add(i)
            s.add(n//i)
    return sum(list(s))
def seive(n):
    z = [False]*(n+1)
    for i in range(n+1):
        if sum_fac(i) > 2*i:
            z[i] = True
    return z
z = seive(20161)
for _ in range(int(input())):
    n = int(input())
    if n > 20161:
        print('YES')
    else:
        flag = False
        for i in range(1, n):
            if z[i] and z[n-i]:
                print('YES')
                flag = True 
                break
        if not flag:
            print('NO')