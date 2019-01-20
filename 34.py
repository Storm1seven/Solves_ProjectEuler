import math
n = int(input())
s = 0
for i in range(10, n+1):
    c = 0
    for j in str(i):
        c+=math.factorial(int(j))
    if c%i == 0:
        s+=i
print(s)