s = 0
for _ in range(int(input())):
    n = input()
    n = n[:15]
    s+=int(n)
print(str(s)[:10])