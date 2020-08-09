# https://dmoj.ca/problem/ccc19s2
# https://dmoj.ca/submission/2243893

from sys import exit
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False    
    return True

import sys
for i in range(int(input())):
    case = int(sys.stdin.readline())
    gap = 0
    while True:
        if gap==0:
            if isPrime(case):
                print(str(case)+' '+str(case))
                break
        if isPrime(case-gap) and isPrime(case+gap):
            print(str(case-gap)+' '+str(case+gap))
            break
        gap+=1