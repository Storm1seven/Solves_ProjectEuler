n= int(input())
inp=[]
for i in range (n):
    inp.append(int(input()))
for i in inp:
    fib=[1, 2]
    while True:
        if ((fib[-1]+fib[-2])<i):
            fib.append(fib[-1]+fib[-2])
        else:
            break
    fib=fib[1::3]
    print(sum(fib))
