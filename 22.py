import string
from collections import defaultdict
n = int(input())
a =[]
for _ in range(n):
	a.append(input())
a.sort()
q = int(input())
d = { k: v for k, v in zip(string.ascii_uppercase, range(1, len(string.ascii_uppercase)+1))}
val = defaultdict(int)
for i in range(len(a)):
	t = 0
	for j in a[i]:
		t+=d[j]
	val[a[i]]+=(i+1)*(t)
for _ in range(q):
	print(val[input()])