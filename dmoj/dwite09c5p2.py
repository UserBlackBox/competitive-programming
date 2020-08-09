# https://dmoj.ca/problem/dwite09c5p2
# https://dmoj.ca/submission/2242381

import bisect
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103]
for x in range(5):
    n = int(input())
    idx = bisect.bisect_left(primes,n)
    if primes[idx] == n:
        right = primes[idx+2]
        left = primes[idx-2]
    else:
        right = primes[idx+1]
        left = primes[idx-2]
    if n-left < right-n:
        print(left)
    else:
        print(right)