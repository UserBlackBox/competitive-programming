# https://dmoj.ca/problem/dwite07c5p2
# https://dmoj.ca/submission/2191082

import math

for a in range(5):
    num = int(input())
    factors = []

    while num % 2 == 0:
        factors.append(2)
        num/=2
    
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            factors.append(i)
            num/=i
    
    if num > 2:
        factors.append(num)
    
    if len(factors) == 1:
        print(0)
    else:
        print(len(factors))