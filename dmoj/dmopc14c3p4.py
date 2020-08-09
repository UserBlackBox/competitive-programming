# https://dmoj.ca/problem/dmopc14c3p4
# https://dmoj.ca/submission/2230668
# written for pypy2

import sys
from itertools import repeat
from math import sqrt
from operator import mul
import bisect
t = int(sys.stdin.readline())

def primeFactor(num):
    if num == 1:
        return [1]
    primes = []
    while num%2==0:
        primes.append(2)
        num/=2
    for i in range(3,int(sqrt(num))+1,2):
        while num%i==0:
            primes.append(i)
            num/=i
    if num>2:
        primes.append(int(num))
    return primes

cases = []

for i in repeat(None,t):
    cases.append(tuple(map(int,sys.stdin.readline()[:-1].split())))

numDict = {1:[1]}

for j in range(min([x[1] for x in cases]),max(x[2] for x in cases)+1):
    if j == 1:
        continue
    primes = primeFactor(j)
    count = {}
    for x in primes:
        try:
            count[x] += 1
        except KeyError:
            count[x] = 1
    for x in count.keys():
        count[x] += 1
    factors = reduce(mul,count.values())
    try:
        numDict[factors].append(j)
    except KeyError:
        numDict[factors] = [j]

for i in cases:
    try:
        left = bisect.bisect_left(numDict[i[0]],i[1])
        right = bisect.bisect_right(numDict[i[0]],i[2],lo=left)
        print len(numDict[i[0]][left:right])
    except KeyError:
        print 0