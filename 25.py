a = 1
b = 1
z = [0]*5001
z[1] = 1
cur_dig = 1
count = 2
while (cur_dig!=5000):
	c = a+b
	count+=1
	if cur_dig+1 == len(str(c)):
		cur_dig+=1
		z[cur_dig]=count
	a = b
	b = c
print(z)
for _ in range(int(input())):
	print(z[int(input())])