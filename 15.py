from math import factorial as fact
for _ in range(int(input())):
    n, m = map(int, input().split())
    print((fact(m + n) // (fact(m) * fact(n))) % 1000000007)
