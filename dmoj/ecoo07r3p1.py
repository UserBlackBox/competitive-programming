# https://dmoj.ca/problem/ecoo07r3p1
# https://dmoj.ca/submission/2244377

def soe(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    primes = []
    for p in range(3, n+1): 
        if prime[p]: 
            primes.append(p)
    return primes

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False    
    return True

import bisect
cases = []
for x in range(5):
    cases.append(int(input()))
primes = soe(max(cases))
for i in cases:
    if isPrime(i):
        print(str(i)+' = '+str(i))
        continue
    
    if i%2==0:
        p = 0
        for j in reversed(primes):
            if j > i/2:
                continue
            left = bisect.bisect_left(primes,i-j)
            if left >= len(primes):
                pass
            elif primes[left] == i-j:
                p = j
                break
        if p != 0:
            print(str(i)+' = '+str(p)+' + '+str(i-p))
            continue

    p = 0
    q = 0
    r = 0
    for j in range(len(primes)-1,-1,-1):
        if primes[j] > i/3:
            continue
        for k in range(len(primes)-1,j-1,-1):
            if primes[j]+primes[k] > i/3*2:
                continue
            left = bisect.bisect_left(primes,i-primes[j]-primes[k])
            if left >= len(primes):
                pass
            elif primes[left] == i-primes[j]-primes[k]:
                p = primes[j]
                q = primes[k]
                r = i-primes[j]-primes[k]
                break
        if p != 0 or q != 0 or r != 0:
            break
    p,q,r = sorted([p,q,r])
    print(str(i)+' = '+str(p)+' + '+str(q)+' + '+str(r))