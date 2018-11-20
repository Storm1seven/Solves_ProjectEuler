import math
import functools
for i in range(int(input())):
    print(functools.reduce(lambda x,y: x*y//math.gcd(x,y), range(1,(int(input())+1))))