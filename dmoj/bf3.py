# https://dmoj.ca/problem/bf3
# https://dmoj.ca/submission/2243880

from sys import exit
import math
n = int(input())

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False    

    return True

while True:
    if isPrime(n):
        print(n)
        exit(0)
    n+=1