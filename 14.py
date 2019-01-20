def step(n):
    count = 0
    if n == 1:
        return 0
    if z[n] != 0:
        return z[n]
    else:
        if n%2 == 0:
            count+=1
            count+=step(n//2)
        else:
            count+=1
            count+=step(3*n + 1)
    z[n]+=count
    return count
z = [0]*10000000
for i in range(1, 5* 10**6):
    step(i)
m = 0
index = 1
for i in range(1, len(z)):
    if z[i] < m:
        z[i] = index
    else:
        m = z[i]
        index = i
        z[i] = i
print(z)