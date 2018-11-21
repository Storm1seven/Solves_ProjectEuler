for _ in range(int(input())):
    n, ans = int(input()), []
    for a in range(3, n // 3 + 1):
        b = int((n ** 2 - 2 * n * a)/(2 * (n - a)))
        ifa ** 2 + b ** 2 == (n - a - b) ** 2:
        	ans.append(a * b * (n - a - b))
    if len(ans) == 0:
    	print(-1)
    else:
    	print(max(ans))